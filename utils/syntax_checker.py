import re

def SyntaxCheck(email = str()) -> bool:
    """
    SyntaxCheck:
    This function checks if the email is written in a correct format. Returns true if written correctly and false otherwise.
    input: 
    email : str
    output: boolean

    """
    if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
        return True
    return False