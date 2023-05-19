# EmailValidator

A email syntax and deliverability validator written in Python. Validates syntax, disposable, dns and smtp.

The software gives requires an email address or a list of them. For each email, the software first checks if the email format is correct, then checks if it is a disposable email, then run through its MX record and then SMTP connection to determine if the email is valid. The software also uses multithreading to process list quicker.

## Usage



### Installation

In order to use this tool, you need to have Python 3.0 or later installed.

You will need Flask, which can be installed using pip:

```python
$ pip install -U Flask
```

You also need to install a DNS toolkit for Python

```python
$ pip install dnspython
```

Last, install PyQt5 to run the GUI

```python
$ pip install PyQt5
```

### Overview

- `disposable_checker.py` - Checks if the email is part of one of the many domains where temporaily emails are created.
- `mx_checker.py` - A function that checks for the domain's MX record
- `smtp_checker.py` - A function that checks if email is valid via SMTP connection
- `syntax_checker.py` - A function that checks if the email is in the correct format

---

- `input_parser.py` - turns the input from the GUI to python variable for python scripts
- `test_case.py` - a list of test cases for the software

### Quick Start
Run main.py and it will shows a GUI. Drag the email list that you want to validate and enjoy!

