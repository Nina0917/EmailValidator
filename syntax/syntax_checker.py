def SyntaxCheck(email = str()) -> bool:
    # Checks for @
    allowed_chars = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-."))
    if email.count("@") == 1:
        name, domain = email.split("@")
        if name == "":
            return False
        # check to see if name is valid
        nameSet = set(name)
        if not nameSet.issubset(allowed_chars):
            return False
            # check if any dash, underscore and period follows a char or number
        if name.endswith("-") or name.endswith("_") or name.endswith("."):
            return False
        
        # Verify domain
        allowed_chars = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"))
        if domain.count(".") == 1:
            domainName, extension = domain.split(".")
            if domainName == "":
                return False
            domainNameSet = set(domainName)
            if not domainNameSet.issubset(allowed_chars):
                return False
            if len(extension) >= 2:
                return True
    return False