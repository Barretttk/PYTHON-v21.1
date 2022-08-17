from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
#==================================
#import models from models folder
#==================================

from flask_app.models import model_user

#===========  CREATE  =================

@app.route('/user/create', methods=['POST'])
def create():
    # validate
    if not model_user.User.validate(request.form):
        return redirect("/")

    #hash  
    hash_password = bcrypt.generate_password_hash(request.form['password'])

    #create
    data = {
        **request.form,
        'password' : hash_password
    }
    id = model_user.User.create(data)

    #store ID inot session
    session["uuid"] = id
    return redirect("/")

#===========  SHOW  =================

@app.route("/user/<int:id>")
def user_show(id):
    return render_template("user_show.html")

#===========  EDIT  =================

@app.route("/user/<int:id>/edit")
def user_edit(id):
    return render_template("user_edit.html")

#===========  UPDATE  =================

@app.route("/user/<int:id>/update", methods = ["post"])
def user_update(id):
    return redirect("/")

#===========  DELETE  =================

@app.route("/user/<int:id>/delete")
def user_delete(id):
    return redirect("/")





