from cmath import log
from flask import Flask
from flask import render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = "ofghsgogdoigsdikn"

@app.route("/")
def form():


    return render_template("index.html")



@app.route("/result")
def submitted_info():
    

    return render_template("result")





if __name__=="__main__":
    app.run(debug=True)