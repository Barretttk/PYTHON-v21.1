
from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#==================================
#import models from models folder
#==================================

from flask_app.models import model_user

#=================  LOGOUT  =================

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

#=================  LOGIN  ===================

@app.route('/user/login', methods=['POST'])
def user_login():
# validate
    model_user.User.validate_login(request.form)

#store id in session
    existing_user = model_user.User.get_one_by_email(request.form)

# if user existing 
    if existing_user != None:
        if not bcrypt.check_password_hash(existing_user.password, request.form["password"]):
            flash("wrong credentials", "err_user_password_login")

        session["first_name"] = existing_user.first_name
        session["email"] = existing_user.email
        session["uuid"] = existing_user.id

        return redirect("/dashboard")
    else:
        return redirect("/")

#================  Registration  =================

@app.route('/user/registration', methods=['POST'])
def process_registration():
    # validate

    if not model_user.User.validate_registration(request.form):
        return redirect("/")

    #Verify user already exists

    user_exists = model_user.User.get_one_by_email(request.form)
    if user_exists == True:
        flash("This Emails already exsist. ", "err_reg_email")
        return redirect("/")

    #hash  
    hash_password = bcrypt.generate_password_hash(request.form['password'])

    #create
    data = {
        **request.form,
        'password' : hash_password
    }
    user_id = model_user.User.create(data)

    #store ID into session
    session["first_name"] = data["first_name"]
    session["email"] = data["email"]
    session["uuid"] = user_id

    return redirect("/dashboard")

#================  SHOW  =================
@app.route("/user/<int:id>/")
def user_show(id):
    return render_template("user_edit.html")


#================  EDIT  =================

@app.route("/user/<int:id>/edit")
def user_edit(id):
    return render_template("user_edit.html")

#================  UPDATE  =================

@app.route("/user/<int:id>/update", methods = ["post"])
def user_update(id):
    return redirect("/")

#================  DELETE  =================

@app.route("/user/<int:id>/delete")
def user_delete(id):
    return redirect("/")





