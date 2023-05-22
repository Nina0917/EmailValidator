import smtplib
import time
import dns.resolver
import socket

def check_email_smtp(email):
    max_retries = 2
    retry_delay = 2 
    """Ping the email address via SMTP. Return true if successful and false if not"""
    for _ in range(max_retries):
        try:
            domain = email.split('@')[1]
            mx_records = dns.resolver.resolve(domain, 'MX', tcp=True, lifetime=90)
            mx_record = str(mx_records[0].exchange)
            server = smtplib.SMTP()
            host = socket.gethostname()
            time.sleep(1)
            server.connect(mx_record)
            server.ehlo(host)
            server.mail('me@outlook.com')
            code, _ = server.rcpt(email)
            server.quit()
            if code == 250:
                return True
            return False
        except smtplib.SMTPConnectError:
            # Connection error, retry after delay
            print("Connection error. Retrying...")
            time.sleep(retry_delay)
        except smtplib.SMTPServerDisconnected:
            # Connection unexpectedly closed, retry after delay
            print("Connection unexpectedly closed. Retrying...")
            time.sleep(retry_delay)
        except (UnicodeError, IndexError, dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return False
    return False