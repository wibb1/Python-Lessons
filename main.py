import smtplib
import time
from email.message import EmailMessage
import sqlite3

import requests
import selectorlib
from dotenv import dotenv_values

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


connection = sqlite3.connect("data.db")


def scrape(url):
    # Scrape the page source from the URL.
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def parse_row(extracted):
    e_row = extracted.split(", ")
    return [item.strip() for item in e_row]


def store(extracted):
    e_row = parse_row(extracted)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?, ?)", e_row)
    connection.commit()


def read(extracted):
    band, city, date = parse_row(extracted)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows


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
            row = read(extracted_data)
            if not row:
                store(extracted_data)
                send_email(message="New Event Found!")
        time.sleep(60 * 60 * 24)
