from flask_app import app
from flask import render_template, redirect, request, session

#==================================
#import models from models folder
#==================================

from flask_app.models. import User
from flask_app.models.  import  


@app.route("/")
def index(): 

    return render_template ("index.html")



@app.route('/create', methods=['POST'])
def create_burger():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Burger.validate_burger(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    Burger.save(request.form)
    return redirect("/burgers")