
from .emails import email_domain_loader

class DisposableEmailChecker():
    """
    Check if an email is from a disposable email service
    """

    message = 'Blocked email provider.'
    code = 'invalid'
    whitelist = []

    def __init__(self, message=None, code=None, whitelist=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if whitelist is not None:
            self.whitelist = whitelist

    def is_disposable(self, email):

        name, domain = email.split(sep="@")
        if domain in email_domain_loader():
            return False
        else:
            return True



