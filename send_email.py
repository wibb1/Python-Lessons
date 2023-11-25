import smtplib
import ssl
from dotenv import dotenv_values


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    config = dotenv_values(".env")
    username = config["USERNAME"]
    password = config["PASSWORD"]
    receiver = "willcampbell030@gmail.com"
    context = ssl.create_default_context()
    outgoing_message = f"""
Subject: News Updates from {receiver}

From: {receiver}
{message}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, outgoing_message)


if __name__ == '__main__':
    send_email("hello")
