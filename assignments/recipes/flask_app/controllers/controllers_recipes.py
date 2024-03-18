
from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#==================================
#import models from models folder
#==================================

from flask_app.models import model_recipe


@app.route("/recipes")
def show_recipes():
    #validate user is logged in
    if "email" not in session:
        return redirect("/")

    list_recipes = model_recipe.Recipe.get_all_with_users()
    return render_template("dashboard.html", list_recipes = list_recipes)

#============= NEW RECIPE PAGE==================

@app.route("/recipe/new")
def create_recipes():
        #validate

        if "email" not in session:
            return redirect("/")
        else:
            return render_template("create.html")

#================= ADD NEW RECIPE =================    

@app.route("/recipe/new", methods = ["post"])
def create_recipe():
    if model_recipe.Recipe.validate_recipe(request.form) == False:
        return redirect("/recipe/new")

    data = {
        **request.form,
        "user_id" : session["uuid"]
    }
    user_id = model_recipe.Recipe.create(data)

    return redirect("/recipes")

#===================== SHOW RECIPES=====================

@app.route("/recipes/<int:id>")
def display_one(id):
    if "email" not in session:
            return redirect("/")

    data = {
        "id" : id
    }

    current_recipe = model_recipe.Recipe.get_one_with_user(data)
    return render_template("show.html", current_recipe = current_recipe)


#================  VIEW TO EDIT  =================

@app.route("/recipes/<int:id>/update")
def display_update_recipe(id):
    if "email" not in session:
            return redirect("/")
    data = {
        "id" : id
    }
    current_recipe = model_recipe.Recipe.get_one_with_user(data)
    return render_template("update_recipe.html", current_recipe = current_recipe)

#================  UPDATE  =================

@app.route("/recipes/<int:id>/update", methods = ["post"])
def update(id):
    if model_recipe.Recipe.validate_recipe(request.form) == False:
        return redirect(f"/recipes/{id}/update")
        
    recipe_data = {
        **request.form,
        "id" : id,
        "user_id" : session ["uuid"]
    }
    model_recipe.Recipe.update_one( recipe_data )
    return redirect("/recipes")

#================  DELETE  =================

@app.route("/recipes/<int:id>/delete")
def delete_recipe(id):
    model_recipe.Recipe.delete_one({"id" : id})
    return redirect("/")

