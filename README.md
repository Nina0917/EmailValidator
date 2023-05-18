# EmailValidator

Checks if the email is valid using many tools and optimization techique.

How the software works:
The software gives requires an email address or a list of them. For each email, the software first checks if the email format is correct, then checks if it is a disposable email, then run through its MX record and then SMTP connection to determine if the email is valid. The software also uses multithreading to process list quicker. 

Files:
disposable_checker.py - Checks if the email is part of one of the many domains where temporaily emails are created
email.py - A list of disposable email domain
mx_checker.py - A function that checks for the domain's MX record
smtp_checker.py - A function that checks if email is valid via SMTP connection
syntax_checker.py - A function that checks if the email is in the correct format
input_parser.py - turns the input from the GUI to python variable for python scripts
test_case.py - a list of test cases for the software

