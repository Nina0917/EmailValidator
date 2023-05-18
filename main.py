from flask import Flask
import threading
from utils.input_parser import parse_csv_file1, parse_csv_file
from utils.syntax_checker import SyntaxCheck
from utils.mx_checker import MXCheck
from utils.smtp_checker import check_emails_smtp, check_email_smtp
from utils.disposable_checker import DisposableEmailChecker
from utils import emails
import csv

app = Flask(__name__)

# flask --app main run
@app.route('/')
def validate_email(email):
    if not SyntaxCheck(email):
        return False
    if not DisposableEmailChecker().is_disposable(email):
        return False
    if not MXCheck(email):
        return False
    # if not check_email_smtp(email):
    #     return False
    return True

def process_chunk(data, results, lock):
    chunk_results = {}
    for email, value in data.items():
        if not validate_email(email):
            chunk_results[email] = value
        else:
            chunk_results[email] = 'Valid'
    with lock:
        results.update(chunk_results)

def write_results_to_csv(results, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for email, value in results.items():
            writer.writerow([email, value])

def main():
    #file_path = 'data/ .csv'
    file_path = 'data/list.csv'
    output_file_path = 'data/results.csv'  
    chunk_size = 2 
    data = parse_csv_file(file_path)
    chunks = [dict(list(data.items())[i:i+chunk_size]) for i in range(0, len(data), chunk_size)]

    results = {}
    lock = threading.Lock()
    threads = []

    for chunk in chunks:
        thread = threading.Thread(target=process_chunk, args=(chunk, results, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    write_results_to_csv(results, output_file_path)
    print("Results written to", output_file_path)

if __name__ == "__main__":
    main()
