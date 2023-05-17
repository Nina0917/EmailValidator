import re

def SyntaxCheck(email = str()) -> bool:
    """
    This function checks if the email is written in a correct format. Returns true if
    written correctly and false otherwise.
    """
    if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
        return True
    return False