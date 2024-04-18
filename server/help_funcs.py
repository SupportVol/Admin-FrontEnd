"""
This file has all of the small funtions which I use mostly
"""

import base64
import smtplib
from email.mime.text import MIMEText
import requests
from server import *


def log_ip_address(url_trying_to_access: str, ip_address: str) -> None:
    db = cluster["ips"]
    collection = db["ips"]
    collection.insert_one(
        {
            "ip_address": ip_address,
            "url_trying_to_access": url_trying_to_access,
            "time": datetime.datetime.now(),
        }
    )


def encode(message: str) -> bytes:
    """
    Encode string for privacy and encryption.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64encode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def decode(message: str) -> bytes:
    """
    Decode string for privacy and encryption.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64decode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def send_email(subject: str, email_to: str, body: str) -> None:
    """
    Send Emails for 2 fac auth and other notifications
    """
    EmailAdd = "ranugagamage@gmail.com"
    Pass = "Ranuga D 2008"
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = EmailAdd
    msg["To"] = email_to
    try:
        s = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
        s.login(user=EmailAdd, password=Pass)
        s.sendmail(EmailAdd, email_to, msg.as_string())
        s.quit()
    except:
        server = smtplib.SMTP_SSL("smtp.googlemail.com", 465)
        server.login(EmailAdd, Pass)
        server.sendemail(EmailAdd, email_to, msg.as_string())


def login_verification():
    return "uid" in session