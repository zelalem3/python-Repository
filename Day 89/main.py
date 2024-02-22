from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clear", methods=["POST"])
def clear():
    request.form.get("text")




if __name__ == "__main__":
    app.run(debug=True, port=8000)