import smtplib as smtp
import ssl
from dotenv import dotenv_values


def create_message(email, subject, message):
    return f"""Subject: New Email from {email} concerning {subject}\n
From: {email}
Topic: {subject}
\n {message}
"""


def send_email(email, subject, message):
    host = 'smtp.gmail.com'
    port = 465
    configure = dotenv_values(".env")
    username = configure['USERNAME']
    password = configure['PASSWORD']
    context = ssl.create_default_context()
    outgoing_msg = create_message(email, subject, message)

    with smtp.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, outgoing_msg)


if __name__ == '__main__':
    send_email("example@example.com", "Test Subject", "Test message")
