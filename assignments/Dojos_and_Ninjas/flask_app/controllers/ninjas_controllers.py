from flask_app import app
from flask import render_template, redirect, request, session


from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

# Route to new ninjas page
# Route for creating new ninja

# ====================================
# Show all  NINJAS
# ====================================

@app.route("/show_ninjas")
def dojos_ninjas():
    all_ninjas = Ninja.show_all_ninjas()
    print(all_ninjas)
    return render_template("show.html",all_ninjas = all_ninjas)


@app.route("/new_ninja")
def ninja():
    dojo_id = Dojo.show_all_dojos()
    return render_template("new_ninja.html", dojo_id=dojo_id)


@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    print(request.form)
    Ninja.create_ninja(request.form)
    return redirect(f"/show/{request.form['dojo_id']}")


@app.route("/show/<int:id>")
def showdojo(id):
    query_data = {
        "id": id
    }
    showdojo = Dojo.showboth(query_data)
    return render_template("show.html", showdojo=showdojo)

