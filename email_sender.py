from email.message import EmailMessage
import os
import ssl
import smtplib

# read sender from environment variable
email_sender = os.getenv("GMAIL_SENDER")
# generate app password (https://myaccount.google.com/apppasswords) and store in environment variable
email_password = os.getenv("GMAIL_APP_PASSWORD")
# create temporary email (https://temp-mail.org/en) and store email address in environment variable
email_receiver = os.getenv("GMAIL_RECEIVER")

subject = "Test email"
body = """
This is a test of the emergency broadcast system...  this is only a test...  BEEEEEEEEEEEEEP!!
"""

message = EmailMessage()
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, message.as_string())