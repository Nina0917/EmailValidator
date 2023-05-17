import smtplib
import dns.resolver
import socket

def check_email_smtp(email):
    try:
        domain = email.split('@')[1]
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
        server = smtplib.SMTP()
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

# # Example usage
# email_list = ["example1@example.com", "jwovsndoisjjsdifeh@gmail.com", "example3@example.com"]
# results = check_emails_smtp(email_list)
# print(results)
