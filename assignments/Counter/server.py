from cmath import log
from flask import Flask
from flask import render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = "ofghsgogdoigsdikn"

@app.route("/")
def counter():
    if "counter" not in session:
        session ["counter"] = 0
    session ["counter"] += 1

    return render_template("index.html", counter = session["counter"])



@app.route("/destroy_session")
def destroy_session():
    session["count"] = -1

    return redirect("/")



@app.route("/two_button")
def two_button():
    session ["count"] +=1

    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)