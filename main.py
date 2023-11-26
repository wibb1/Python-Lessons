from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

stations = pd.read_csv("data/stations.txt", skiprows=17)
stations = stations[['STANAME                                 ', 'STAID']]


@app.route("/home/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/api/v1/<station>/<date>")
def temp(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}


if __name__ == '__main__':
    app.run(debug=True)
