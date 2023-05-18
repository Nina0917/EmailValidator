import csv
"""input small file """
def parse_csv_file(filename):
    data = {}
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[0]
            validity = row[1]
            data[email] = "invalid"
    
    return data

"""input large file and all email default invalid"""
def parse_csv_file1(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[0]
            data[email] = "invalid"

    return data

