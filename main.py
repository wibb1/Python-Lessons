from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

df = pd.read_csv("dictionary.csv")


@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def definition(word):
    response = df.loc[df['word'] == word]['definition'].squeeze()
    return {"definition": response, "word": word}


if __name__ == '__main__':
    app.run(debug=True, port=5001)
