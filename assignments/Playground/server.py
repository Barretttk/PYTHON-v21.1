from flask import Flask
from flask import render_template, redirect, session, request
app = Flask(__name__)


@app.route("/play")
def index():
    print("welcome")
    return render_template("home.html")

@app.route("/play/<int:num>")
def add_block(num):
    return render_template("index.html", num_block = num)

@app.route("/play/<int:num>/<string:color>")
def change_color(num, color):
    return render_template("index.html", num_block = num, color = color)



if __name__=="__main__":
    app.run(debug=True)