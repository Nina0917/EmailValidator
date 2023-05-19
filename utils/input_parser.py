import csv
"""
parse_csv_file:
this method parse the input csv file to a dictionary of emails, with default value "invalid"
input: file path
output: dictionary
 """

def parse_csv_file(filename):
    data = {}
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[0]
            validity = row[1]
            data[email] = "Invalid"
    
    return data

"""
parse_csv_file1:
this method parse the input csv file to a dictionary of emails, with default value "invalid"
input: file path
output: dictionary
 """
def parse_csv_file1(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[0]
            data[email] = "Invalid"

    return data

