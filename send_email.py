import smtplib
import os
from email.mime.text import MIMEText


def send_email(receiver, height, average_height, count):
    sender = "sanydge@gmail.com"
    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and " \
              "that " \
              "is calculated out of <strong>%s</strong> people. <br> Thanks!" % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = receiver
    msg['From'] = sender

    # Mailjet
    with smtplib.SMTP(os.getenv("SMTP_HOST"), os.getenv("SMTP_PORT")) as server:
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        server.sendmail(sender, receiver, msg.as_string())

