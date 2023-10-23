import csv
import shutil
import webbrowser


with open("weather.csv", 'r') as file:
    data = dict(csv.reader(file))

print(data)


city = input("Enter a city: ").title()

if data.__contains__(city):
    print(city, data[city])


shutil.make_archive("output", "zip", "exercise7")

user_term = input("Enter a search term").replace(" ", "+")

webbrowser.open(f"https:google.com/search?q={user_term}")
