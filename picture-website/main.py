import streamlit as st
import requests
from dotenv import dotenv_values


def get_response():
    config = dotenv_values('.env')
    API_KEY = config['API_KEY']
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    try:
        resp = requests.get(url, timeout=1, verify=True)
        resp.raise_for_status()
        data = resp.json()
        return data
    except requests.exceptions.HTTPError as er:
        print("HTTP Error")
        print(er.args[0])
    except requests.exceptions.ReadTimeout as er:
        print("Time out")
        print(er.args[0])
    except requests.exceptions.ConnectionError as er:
        print("Connection error")
        print(er.args[0])
    except requests.exceptions.RequestException as er:
        print("Exception request")
        print(er.args[0])


def print_data(data):
    st.title(data["title"])
    st.image(data["url"])
    data["explanation"]


if __name__ == '__main__':
    data = get_response()
    print_data(data)