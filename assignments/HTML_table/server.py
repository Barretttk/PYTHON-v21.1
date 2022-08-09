from flask import Flask
from flask import render_template, redirect, session, request
app = Flask(__name__)



@app.route("/lists")
def render_users():

    person_info = [
        {'First_name' : 'Michael', 'Last_name' : 'Choi , Full_Name : Michael Choe'},
        {'First_name' : 'John', 'Last_name' : 'Supsupin, Full_Name : John Supsupin'},
        {'First_name' : 'Mark', 'Last_name' : 'Guillen, Full_Name : Mark Guillen'},
    ]

    return render_template("index.html", person_info = person_info)



if __name__=="__main__":
    app.run(debug=True)