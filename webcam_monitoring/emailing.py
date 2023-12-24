import imghdr
import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values
import threading


def send_email(image_path):
    lock = threading.Lock()
    lock.acquire()
    host = "smtp.gmail.com"
    port = 587
    config = dotenv_values(".env")
    username = config["USERNAME"]
    password = config["PASSWORD"]
    receiver = "willcampbell030@gmail.com"

    email_message = EmailMessage()
    email_message["Subject"] = "New Sighting"
    email_message.set_content(f"A new sighting occurred!")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    lock.release()
    gmail = smtplib.SMTP(host, port)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()


if __name__ == '__main__':
    send_email("test_image/file_example_PNG_500kB.png")
