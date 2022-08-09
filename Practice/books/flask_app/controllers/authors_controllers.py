from flask_app import app
from flask import render_template, redirect, request, session
#==================================
#import models from models folder
#==================================

from flask_app.models. Authors import Authors 
from flask_app.models. Books import Books


@app.route("/")
def index():

    return render_template ("HOME.html")


#     @app.route("/")
# def dojos():