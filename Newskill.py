import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "this is a test email from python"
senderEmail = "c0d3ra11y@gmail.com"
receiverEmail = "c0d3ra11y@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = senderEmail
message["to"] = receiverEmail
message["subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("sending email")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(senderEmail, password)
    server.sendmail(senderEmail,receiverEmail, message.as_string())
    
    print("email sent")