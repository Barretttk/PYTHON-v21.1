import uuid
from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify

#==================================
#import models from models folder
#==================================

from flask_app.models.model_user import model_users


@app.route("/")
def index():
    if "uuid" is
        return
    return render_template

@app.route("/Login")
def index(): 
    return render_template ("login.html")



@app.route('/Login/create', methods=['POST'])
def create():
# validator

    "first_name" : request.form["first_name"]
    "last_name" : request.form["last_name"]
    "email" : request.form["email"]
    "password" : request.form["password"]
    }

    # validate form

    is_valid = .validator(request,form)

    return redirect("/")




