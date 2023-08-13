import smtplib, ssl
from password import new_password


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "michaelcharles10904@gmail.com"
receiver_email = "michaelcharles10904@gmail.com"
password = new_password
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)