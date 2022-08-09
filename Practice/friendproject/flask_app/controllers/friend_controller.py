
from flask_app import app
from flask import render_template, redirect, session, request


# import the class from friend.py
from flask_app.models.friend import Friend

#====================================
# Read ALL Routes
#====================================

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    all_friends = Friend.get_all()
    print(all_friends)
    return render_template("index.html", all_friends = all_friends)

#====================================
# Read One Route
#====================================

# rendeing a Id from linking information on HTML sheet
@app.route("/friend/<int:friend_id>")
def one_friend(friend_id):
    query_data = {
        "friend_id" : friend_id
    }
    one_friend = Friend.get_one_friend(query_data)
    return render_template("show_one.html", one_friend = one_friend)

#====================================
# Create One Route
#====================================

@app.route("/friend/new")
def add_friend():

    return render_template("add_friend.html")

@app.route("/friend/create", methods = ["POST"])
def create_friend():

    # 1 colletct information from our form to send to Query
    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"],
        #cast as a int
        "age" : int(request.form["age"]),
    }
    print(query_data)
    #2 call on query from our model file
    new_friend_id = Friend.create_new_friend(query_data)

    #3 redirect elsewhere once query is done
    return redirect(f"/friend/{new_friend_id}")



if __name__ == "__main__":
    app.run(debug=True)