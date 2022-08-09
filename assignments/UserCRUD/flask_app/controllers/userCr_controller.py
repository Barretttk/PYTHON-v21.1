
from flask_app import app
from flask import render_template, redirect, session, request


# import the class from (.py)
from flask_app.models.user import User

#====================================
# Show ALL Routes
#====================================

@app.route("/")
def index():
    # call the get all classmethod to get all 
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

#====================================
# Show one Route
#====================================

# rendeing a Id from linking information on HTML sheet
@app.route("/show/<int:user_id>")
def one_user(user_id):
    query_data = {
        "user_id" : user_id
    }
    one_user = User.get_one_user(query_data)
    return render_template("index_show.html", one_user = one_user)

#====================================
# Delete one Route
#====================================

@app.route("/delete/<int:id>")
def delete_one_user(id):
    query_data = {
        "user_id" : id
    }
    User.delete_one_user(query_data)

    return redirect("/")

#====================================
# Route to edit page
# ===================================

@app.route("/edit/<int:id>")
def edit_user(id):
    query_data = {
        "user_id" : id
    }
    one_user = User.get_one_user(query_data)

    return render_template("index_edit.html", one_user = one_user)

#====================================
# Update User  information 
# ===================================

@app.route("/user/edit/<int:id>", methods = ["POST"])
def update_user(id):
    query_data = {
        "user_id" : id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]

    }
    User.update_one_user(query_data)

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)