import dns
import dns.resolver

def MXCheck(email = str()) -> bool:
    """
    MXCheck:
    This function checks if the mail exchange server exist according to standards of email. Return true if mail exchange server exist and false if not.
    input: 
    email : str
    output: boolean

    """
    # Assume Syntax is valid
    name, domain = email.split(sep="@")
    # Run to see if any MX records exist and return all possible MX
    try:
        MXList = dns.resolver.resolve(domain, "MX", tcp=True)
        MXList = sorted([(r.preference, str(r.exchange).rstrip('.')) for r in MXList])
        for Mx in MXList:
            # Delete Null MX records
            if Mx[1] == ".":
                del Mx
        if len(MXList) != 0:
            return True
        else:
            # MXRecord Not Found
            return False

    except:
        # Attempt to perform fallback measure
        try:
            IpList = dns.resolver.resolve(domain, "A", tcp=True)
        except:
            try: 
                IpList = dns.resolver.resolve(domain, "AAAA", tcp=True)
            except:
                # MXRecord Not Found
                return False
        for ip in IpList:
                ip = (0, str(ip))
        # Check for reject all record
        rejectList = dns.resolver.resolve(domain, "TXT", tcp=True)
        for reject in rejectList:
            if reject.strings == "v=spf1 -all":
                return False
        return True
