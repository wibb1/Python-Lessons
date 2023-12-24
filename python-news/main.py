import requests
from dotenv import dotenv_values
from send_email import send_email


def main():
    config = dotenv_values(".env")
    API_KEY = config['API_KEY']
    topic = 'tesla'
    url = (f"https://newsapi.org/v2/everything?"
           f"q={topic}&"
           f"sortBy=publishedAt&"
           f"apiKey={API_KEY}"
           f"&language=en")
    # handle errors
    request = requests.get(url)
    content = request.json()
    outgoing_message = "Subject: Today's news\n"
    for article in content['articles'][:20]:
        if article['title'] is not None:
            outgoing_message += f"{article['title']}\n\n{article['description']}\n\n{article['url']}\n\n\n"
    send_email(outgoing_message.encode('utf-8'))


if __name__ == '__main__':
    main()
