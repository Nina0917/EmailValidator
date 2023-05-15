import csv

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
#output
"""[{'alesiaconover@cox.net': 'valid'}, {'magormley1@cox.net': 'invalid'}, 
{'lwoodard@cox.net': 'invalid'}, {'stondreau@cox.net': 'valid'}, {'lhutfles@cox.net': 'valid'},
 {'bolivarfamily@cox.net': 'invalid'}, {'ageecrew@cox.net': 'invalid'}, {'0cimei@cox.net': 'invalid'}, 
 {'123aloop1@cox.net': 'invalid'}, {'1350tw@cox.net': 'invalid'}, {'1slgoodman62@cox.net': 'invalid'}, 
 {'187thepigs@cox.net': 'invalid'}, {'2katz2meny@cox.net': 'invalid'}, {'jkaine1994@cox.net': 'valid'}, {'3boyzmom@cox.net': 'valid'}]"""


def parse_csv_file1(filename):
    data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[0]
            data.append(email)

    return data

# Example usage
filename = 'emaillist.csv'
parsed_data1 = parse_csv_file1(filename)
print(parsed_data1)