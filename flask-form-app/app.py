from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import dotenv_values
from flask_mail import Mail, Message

env_config = dotenv_values(".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = env_config["USERNAME"]
app.config["MAIL_PASSWORD"] = env_config['PASSWORD']

db = SQLAlchemy(app)

mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    start_date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route('/', methods=["GET", "POST"])
def index():
    req = request.method
    match req:
        case "POST":
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            start_date = datetime.strptime(request.form["start_date"], "%Y-%m-%d")
            occupation = request.form["occupation"]

            form = Form(first_name=first_name, last_name=last_name, email=email, start_date=start_date,
                        occupation=occupation)
            db.session.add(form)
            db.session.commit()
            end_line = "\n\t"
            outgoing_message = (f"Welcome to the job board {first_name}!\n"
                                f"Here is you information:{end_line}"
                                f"First Name: {first_name}{end_line}"
                                f"Last name: {last_name}{end_line}"
                                f"Email: {email}{end_line}"
                                f"Current occupation: {occupation}{end_line}"
                                f"Start date: {start_date}{end_line}"
                                f"Thank you!")
            message = Message(
                subject="New Form Submission",
                sender=app.config["MAIL_USERNAME"],
                recipients=[email],
                body=outgoing_message
            )
            mail.send(message)

            flash(f"{first_name} Your form was submitted successfully", "success")
            return render_template("index.html")

        case "GET":
            return render_template("index.html")


if __name__ == "__main__":

    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)


