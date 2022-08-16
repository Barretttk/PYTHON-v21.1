from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify

#==================================
#import models from models folder
#==================================

from flask_app.models import model_user

# ================== default routes ===============

@app.route("/")
def index():
    if "uuid" in session:
        return redirect("/dashboard")
    return render_template("landing_page/index.html")

@app.route("/")
def index():
    if "uuid" not in session:
        return redirect("/dashboard")
    return render_template("landing_page/index.html")


@app.route("/", defaults={"path": ''})
@app.route('/<path:path>')
def catch_all(path):
        return 'page not found'
