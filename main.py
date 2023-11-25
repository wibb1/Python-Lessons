import requests
from dotenv import dotenv_values
from send_email import send_email


def main():
    config = dotenv_values(".env")
    API_KEY = config['API_KEY']
    url = f"https://newsapi.org/v2/everything?q=tesla&contry=us&sortBy=publishedAt&apiKey={API_KEY}"
    # handle errors
    request = requests.get(url)
    content = request.json()
    outgoing_message = ''
    for article in content['articles']:
        if article['title'] is not None:
            outgoing_message += (f"{article['title'].strip()}\n"
                                 f"{article['description'].strip()}\n\n")
    send_email(outgoing_message.encode('utf-8'))


if __name__ == '__main__':
    main()
