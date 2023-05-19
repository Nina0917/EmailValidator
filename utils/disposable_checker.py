
from .emails import email_domain_loader


class DisposableEmailChecker():
    """
    DisposableEmailChecker:
    This class used to check if the emails written in a correct format
    Attributes:
    message
    code
    whitelist
    """

    message = 'Blocked email provider.'
    code = 'invalid'
    whitelist = []


    def __init__(self, message=None, code=None, whitelist=None):
        """
        Iitialize an instance of DisposableEmailChecker
        args:
        message
        code
        whitelist
        
        """
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if whitelist is not None:
            self.whitelist = whitelist


    def is_disposable(self, email):
        """
        check if the emails written in a correct format
        input: email
        output:boolean
        """

        name, domain = email.split(sep="@")
        if domain in email_domain_loader():
            return False
        else:
            return True



