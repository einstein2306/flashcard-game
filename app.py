from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def game():
    return render_template("game.html")

@app.route("/subtraction")
def subtraction():
    return render_template("subtraction.html")

@app.route("/multiplication")
def multiplication():
    return render_template("multiplication.html")
    