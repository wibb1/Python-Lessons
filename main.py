import datetime

from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

# Constants
ST_NAME = 'STANAME                                 '
ST_ID = 'STAID'
DATE = '    DATE'
TG = '   TG'

stations = pd.read_csv("data/stations.txt", skiprows=17)
stations = stations[[ST_ID, ST_NAME]]


@app.route("/home/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/api/v1/<station>/<date>")
def temp(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=[DATE])
    temperature = df.loc[df[DATE] == date][TG].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}


@app.route("/api/v1/<station>")
def station_temp(station):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=[DATE])
    station_name = stations.loc[int(station) - 1][ST_NAME]
    return {"station": station_name, "temperatures": df.to_dict(orient='records')}


@app.route("/api/v1/yearly/<station>/<year>")
def station_temp_year(station, year):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    station_name = stations.loc[int(station) - 1][ST_NAME]
    df[DATE] = df[DATE].astype(str)
    temperature = df.loc[df[DATE].str.startswith(str(year))]
    return {"station": station_name, "temperatures": temperature.to_dict(orient='records')}


if __name__ == '__main__':
    app.run(debug=True)
