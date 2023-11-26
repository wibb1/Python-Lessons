from flask import Flask, render_template

app = Flask("__name__")


@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def definition(word):
    response = "this will be a definition of the word"
    return {"definition": response, "word": word.upper()}


if __name__ == '__main__':
    app.run(debug=True, port=5001)
