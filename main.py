import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape():
    # Scrape the page source from the URL.
    response = requests.get(URL, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email():
    print("Email sent")


def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read():
    with open("data.txt") as file:
        return file.read()


if __name__ == '__main__':
    site_data = scrape()
    extracted_data = extract(site_data)
    print(extracted_data)
    if extracted_data != "No upcoming tours":
        if extracted_data not in read():
            store(extracted_data)
            send_email()
