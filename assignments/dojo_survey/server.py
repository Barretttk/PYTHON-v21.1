from flask import Flask
from flask import render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = "ofghsgogdoigsdikn"

@app.route("/")
def form():
    if "data" in session:
        print(session["data"])
        
    return render_template("index.html")

@app.route("/result")
def submitted_info():
    name = session ["name"]
    location = session ["location"]
    languages = session ["languages"]
    comment = session ["comment"]
    agree = session ["agree"]
    print ("submitted_info")

    return render_template("result.html", name = name, languages = languages, location = location, comment = comment, agree = agree)



@app.route("/create", methods=["post"])
def infocreated():
    session["name"] = request.form ["name"]
    session["location"] = request.form ["location"]
    session["languages"] = request.form ["languages"]
    session["comment"] = request.form ["comment"]
    session["agree"] = request.form ["agree"]

    return redirect('/result')




if __name__=="__main__":
    app.run(debug=True)