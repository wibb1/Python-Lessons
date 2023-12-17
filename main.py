import smtplib
import time
from email.message import EmailMessage

import requests
import selectorlib
from dotenv import dotenv_values

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    # Scrape the page source from the URL.
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    with open("data.txt") as file:
        return file.read()


def send_email(message):
    host = "smtp.gmail.com"
    port = 587
    config = dotenv_values(".env")
    username = config["USERNAME"]
    password = config["PASSWORD"]
    receiver = "willcampbell030@gmail.com"

    email_message = EmailMessage()
    email_message["Subject"] = "New Date"
    email_message.set_content(message)

    gmail = smtplib.SMTP(host, port)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()


if __name__ == '__main__':
    while True:
        site_data = scrape(URL)
        extracted_data = extract(site_data)
        print(extracted_data)
        if extracted_data != "No upcoming tours":
            if extracted_data not in read():
                store(extracted_data)
                send_email(message="New Event Found!")
        time.sleep(60)
