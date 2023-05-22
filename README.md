# EmailValidator

A email syntax and deliverability validator written in Python. Validates syntax, disposable, dns and smtp.

The software gives requires an email address or a list of them. For each email, the software first checks if the email format is correct, then checks if it is a disposable email, then run through its MX record and then SMTP connection to determine if the email is valid. The software also uses multithreading to process list quicker.

## Usage

You can either double click on the Email Validator.exe application, or run main.py. The program will shows a GUI. Browse for the email list \(need to be in .csv format\) that you want to validate and enjoy!

### Installation

No installation is required for running EmailValidator.exe.

To run the Python script version of the application, you need to have Python 3.0 or later installed on your system.

Additionally, you need to install the required packages by running the following command:

```python
$ pip install -r requirements. txt
```

### Overview

- `syntax_checker.py` - A function that checks if the email is in the correct format
- `disposable_checker.py` - Checks if the email is part of one of the many domains where temporaily emails are created.
- `mx_checker.py` - A function that checks for the domain's MX record
- `smtp_checker.py` - A function that checks if email is valid via SMTP connection

---

- `input_parser.py` - turns the input from the GUI to python variable for python scripts
- `test_case.py` - a list of test cases for the software

## Potential Improvements

Here are some potential improvements that could be considered for future development:

1. Reduce block by SMTP email servers thus improve accuracy.
2. Improve the accuracy of gibberish checking by expanding training dataset.
3. Optimize the multithreading functionality to maximize processing speed while maintaining stability.
4. Support additional input formats.
