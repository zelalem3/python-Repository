from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)
today = date.today()
year = today.year


@app.route("/")
def hello():
    return render_template("index.html", year=year)


@app.route("/guess/<name>")
def guess(name):
    age = requests.get(f"https://agify.io?name={name}")
    age_data = age.json()
    gender = requests.get(f"https://genderize.io?name={name}")
    gender_data = gender.json()
    name = name.title()
    return render_template("another.html", guess=name, gender=gender_data["gender"], age=age_data["age"])


if __name__ == "__main__":
    app.run(debug=True)
