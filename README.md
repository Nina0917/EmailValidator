# EmailValidator

EmailValidator is a Python-based software tool that validates email syntax and deliverability. It offers comprehensive validation features including syntax checking, disposable email detection, DNS resolution, and SMTP connection verification.

The software requires an email address or a list of them. For each email, the software first checks if the email format is correct, then checks if it is a disposable email, then run through its MX record and then SMTP connection to determine if the email is valid. The software utilizes multithreading to process a list of email addresses efficiently and quickly.

## Usage

There are two versions available for running the EmailValidator tool: an executable (.exe) version and a version designed for Google Colab. These versions have slightly different functionalities:

### Executable Version

1. Double-click the Email Validator.exe file to launch the application (recommended).
2. To run the Python script version of the application, you need to have Python 3.0 or later installed on your system.
Additionally, you need to install the required packages by running the following command:

```python
$  pip install -r /path/to/requirements.txt
```

### Google Colab Version

1. Open the Google Colab notebook using the following link:
   https://colab.research.google.com/drive/1NmTPIamL4L-fIJGXGMVh0_WXNK3qxQFl?usp=share_link
2. In the notebook, you can modify the raw_url variable in the main script to specify your input source. Make sure to use a valid raw GitHub URL for correct execution.

## Explaination Video

https://www.youtube.com/watch?v=nI3y_7JhcPg

## Potential Improvements

Here are some potential improvements that could be considered for future development:

1. Reduce block by SMTP email servers thus improve accuracy.
2. Improve the accuracy of gibberish checking by expanding training dataset.
3. Optimize the multithreading functionality to maximize processing speed while maintaining stability.
4. Support additional input formats.
## Results

The validation results for two versions are stored in results folder. For judges, please view those two folders to see results.
