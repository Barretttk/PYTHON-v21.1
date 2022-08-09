
from flask_app import app
from flask import render_template, redirect, session, request


# import the class from (.py)
from flask_app.models.user import User

#====================================
# Show ALL Routes
#====================================

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    all_users = User.get_all_users()
    print(all_users)
    return render_template("index.html", all_users = all_users)

#====================================
# Go to Create New Route
#====================================

@app.route("/create_new_user")
def new_user():
    
    
    return render_template("index_nu.html")


#====================================
# Create New user Route
#====================================

@app.route("/user/create", methods = ["POST"])
def create_user():


    User.create_user(request.form)
    #request.form returns all user information ^^


    #3 redirect elsewhere once query is done
    return redirect("/")


















if __name__ == "__main__":
    app.run(debug=True)