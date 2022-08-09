from flask_app import app
from flask import render_template, redirect, request, session
#==================================
#import models from models folder
#==================================

from flask_app.models.Books import Books
from flask_app.models. Authors import Authors


@app.route("")
def index():

    return render_template ("index.html")


#     @app.route("/")
# def dojos():