from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def game():
    return render_template("game.html")