import smtplib
import dns.resolver
import socket

def check_email_smtp(email):
    try:
        domain = email.split('@')[1]
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
        server = smtplib.SMTP(timeout=120)
        host = socket.gethostname()
        server.connect(mx_record)
        server.helo(host)
        server.mail('me@outlook.com')
        code, _ = server.rcpt(email)
        server.quit()
        if code == 250:
            return True
        return False
    except (UnicodeError, IndexError, dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, smtplib.SMTPConnectError):
        return False

def check_emails_smtp(emails):
    results = {}
    for email in emails:
        results[email] = check_email_smtp(email)
    return results

# Example usage
email_list = ["alesiaconover@cox.net", "jwovsndoisjjsdifeh@gmail.com", "ijdasjidjkslkew@cox.net"]
results = check_emails_smtp(email_list)
print(results)
