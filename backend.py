from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
READINGS_PER_DAY = 8


def get_data(place, days, units):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units={units}&appid={config['API_KEY']}"
    response = requests.get(url)
    data = response.json()
    return data['list'][:READINGS_PER_DAY * days]


if __name__ == '__main__':
    data1 = get_data('Tokyo', 2)
    print(data1)
    data2 = get_data('Tokyo', 2)
    print(data2)
