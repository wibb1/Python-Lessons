import os

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-10-24&sortBy=publishedAt&apiKey={API_KEY}"
    request = requests.get(url)
    content = request.json()
    if content["status"] == 'ok':
        for article in content['articles']:
            print(article['title'])
            print(article['description'])


if __name__ == '__main__':
    main()
