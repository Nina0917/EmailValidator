# EmailValidator

EmailValidator is a Python-based software tool that validates email syntax and deliverability. It offers comprehensive validation features including syntax checking, disposable email detection, DNS resolution, and SMTP connection verification.

The software requires an email address or a list of them. For each email, the software first checks if the email format is correct, then checks if it is a disposable email, then run through its MX record and then SMTP connection to determine if the email is valid. The software utilizes multithreading to process a list of email addresses efficiently and quickly.

## Usage

There are two versions available for running the EmailValidator tool: an executable (.exe) version and a version designed for Google Colab. These versions have slightly different functionalities:

    # Executable Version
    1. Double-click the Email Validator.exe file to launch the application (recommended).
    2. Alternatively, you can run the main.py file using Python, following the installation instructions provided below.

    #Google Colab Version
    1. Open the provided Google Colab notebook using the following link: 
    
    https://colab.research.google.com/drive/1NmTPIamL4L-fIJGXGMVh0_WXNK3qxQFl?usp=share_link

    2. In the notebook, you can modify the raw_url variable in the main script to specify your input source. Make sure to use a valid raw GitHub URL for correct execution.



### Installation

To use the EmailValidator tool with Python, ensure that you have Python 3.0 or a later version installed on your system. Additionally, install the following dependencies:

Flask: Use the following command to install Flask via pip:

```python
$ pip install -U Flask
```

dnspython: Install the DNS toolkit for Python by running the following command:

```python
$ pip install dnspython
```

PyQt5: Install PyQt5 library to enable the Graphical User Interface (GUI) functionality:

```python
$ pip install PyQt5
```

gibberish_detector: Install the gibberish_detector library, which is used for detecting disposable email addresses:

```python
$ pip install gibberish_detector
```
Once the dependencies are installed, you are ready to run the EmailValidator tool and validate email addresses with ease.

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

