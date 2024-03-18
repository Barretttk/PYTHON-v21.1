from flask_app import app
from flask import render_template, redirect, request, session


from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# ====================================
# Show all DOJOS
# ====================================
# home page


@app.route("/")
def dojos():
    all_dojos = Dojo.show_all_dojos()
    print(all_dojos)
    return render_template("home.html", all_dojos=all_dojos)

# Route to create new Dojo


@app.route("/dojo/create", methods=["POST"])
def create_dojo():

    print(request.form)
    models.dojo.Dojo.create_dojo(request.form)
    return redirect("/")




