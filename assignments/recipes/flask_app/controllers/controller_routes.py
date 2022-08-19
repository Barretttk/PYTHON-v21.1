from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
#==================================
#import models from models folder
#==================================

from flask_app.models import model_user
from flask_app.models import model_recipe

# ================== default routes ===============

@app.route("/")
def index():
    if "uuid" in session:
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "uuid" not in session:
        return redirect("/")
    
    list_recipes = model_recipe.Recipe.get_all_with_users()
    return render_template("dashboard.html", list_recipes = list_recipes, user = model_user.User.get_one({"id":session["uuid"]}))


@app.route('/<path:path>')
def catch_all(path):
        return 'page not found'
