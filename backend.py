from dotenv import dotenv_values
import requests

config = dotenv_values(".env")


def get_data(place, days, view_data):
    from dotenv import dotenv_values
    config = dotenv_values(".env")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={config['API_KEY']}"
    response = requests.get(url)
    content = response.json()
    return content
    # dates = ["2022-25-10", "2023-25-10", "2023-26-12"]
    # temperatures = [25, 11, 10]
    # temperatures = [days * i for i in temperatures]
    # return dates, temperatures


if __name__ == '__main__':
    data = get_data('Tokyo', 5, 'Temperature')
    print(data)
