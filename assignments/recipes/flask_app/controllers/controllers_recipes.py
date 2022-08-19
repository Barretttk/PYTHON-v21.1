
from re import I
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

@app.route("/recipe/new")
def create_recipes():
        #validate

        # if "email" not in session:
        #     return redirect("/")
        # else:
            return render_template("create.html")

@app.route("/recipe/new", methods = ["post"])
def create_recipe():
    if model_recipe.validate_recipe(request.form) == False:
        return redirect("/recipe/new")


    data = {
        **request.form,
        "user_id" : session["uuid"]
    }
    user_id = model_recipe.Recipe.create(data)

    return redirect("/recipes")

#===================== DISPLAY RECIPES=====================

@app.route("/recipes/<int:id>")
def display_one(id):
    # if "email" not in session:
        #     return redirect("/")
    data = {
        "id" : id
    }
    current_recipe = model_recipe.Recipe.get_one_with_user(data)
    return render_template("dashboard.html", current_recipe = current_recipe)