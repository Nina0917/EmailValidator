import dns
import dns.resolver

def MXCheck(email = str()) -> tuple:
    # Assume Syntax is valid
    name, domain = email.split(sep="@")
    # Run to see if any MX records exist and return all possible MX
    try:
        MXList = dns.resolver.resolve(domain, "MX")
        MXList = sorted([(r.preference, str(r.exchange).rstrip('.')) for r in MXList])
        for Mx in MXList:
            # Delete Null MX records
            if Mx[1] == ".":
                del Mx
            print(Mx)
        if len(MXList) != 0:
            return MXList, "MX"
        else:
            # MXRecord Not Found
            return None, ""

    except:
        # Attempt to perform fallback measure
        fallback_record = ""
        try:
            IpList = dns.resolver.resolve(domain, "A")
            fallback_record = "A"
        except:
            try: 
                IpList = dns.resolver.resolve(domain, "AAAA")
                fallback_record = "AAAA"
            except:
                # MXRecord Not Found
                return None, ""
        for ip in IpList:
                ip = (0, str(ip))
        # Check for reject all record
        rejectList = dns.resolver.resolve(domain, "TXT")
        for reject in rejectList:
            if reject.strings == "v=spf1 -all":
                return None
        return IpList, fallback_record

MXCheck("info@keepamericafishing.org")