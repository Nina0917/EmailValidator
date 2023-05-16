import re

def SyntaxCheck(email = str()) -> bool:
    # Checks for @
    if re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
        return True
    return False