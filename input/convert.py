import csv
"""input small file """
def parse_csv_file(filename):
    data = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[0]
            validity = row[1]
            data.append({email:validity})
    
    return data

# Example usage
filename = 'list.csv'
#parsed_data = parse_csv_file(filename)
#print(parsed_data)

"""input large file and all email default invalid"""
def parse_csv_file1(filename):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[0]
            data[email] = "invalid"

    return data

# Example usage
filename = 'emaillist.csv'
parsed_data1 = parse_csv_file1(filename)
print(parsed_data1['aaronvyyahoo.de@t-online.de'])