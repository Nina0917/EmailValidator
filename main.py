
from flask import Flask
import threading
from utils.input_parser import parse_csv_file1,parse_csv_file
from utils.syntax_checker import SyntaxCheck
from utils.mx_checker import MXCheck
from utils.smtp_checker import check_emails_smtp,check_email_smtp
from utils.disposable_checker import DisposableEmailChecker
from utils import emails

app = Flask(__name__)

# flask --app main run
@app.route('/')

def validate_email(email):
    if not SyntaxCheck(email):
        print(1)
        return False
    # if DisposableEmailChecker().is_disposable(email):
    #     print(2)
    #     return False
    if not MXCheck(email):
        print(3)
        return False
    if not check_email_smtp(email):
        print(4)
        return False
    return True

def process_chunk(data):
    results = {}
    for email, value in data.items():
        if not validate_email(email):
            results[email] = value
        else:
            results[email] = 'Valid'
    print(results)
    return results

def main():
    #file_path = 'data/emaillist.csv'
    file_path = 'data/list.csv'
    chunk_size = 2  # Adjust the chunk size as per your requirements
    data = parse_csv_file(file_path)
    print("data",data)
    chunks = [dict(list(data.items())[i:i+chunk_size]) for i in range(0, len(data), chunk_size)]

    threads = []

    for chunk in chunks:
        thread = threading.Thread(target=process_chunk, args=(chunk,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
