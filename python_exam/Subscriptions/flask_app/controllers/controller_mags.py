
import uuid
from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#==================================
#import models from models folder
#==================================

from flask_app.models import model_mag
from flask_app.models import model_user

#============= NEW MAG PAGE==================

@app.route("/mag/add")
def add_mag():
        #validate

        # if "email" not in session:
        #     return redirect("/")
        # else:
            return render_template("mag.html")



#================= ADD NEW MAG =================

@app.route("/mag/add", methods = ["post"])
def create_new_mag():
    # if model_mag.Magazine.validate_mag(request.form) == False:
    #     return redirect("/mag/new")

    data = {
        **request.form,
        "user_id" : session["uuid"]
    }
    user_id = model_mag.Magazine.create(data)

    return redirect("/dashboard")

#================  DELETE  =================

@app.route("/mag/<int:id>/delete")
def delete_recipe(id):
    model_mag.Magazine.delete_one({"id" : id})
    return redirect("/")

# @app.route("/show/<int:id>")
# def display_one(id):
#     if "email" not in session:
#             return redirect("/")

#     mag = {
#         "id" : id
#     }

#     current_magazine = model_mag.Magazine.get_one_with_user(data)
#     return render_template("show.html", current_magazine = current_magazine)

