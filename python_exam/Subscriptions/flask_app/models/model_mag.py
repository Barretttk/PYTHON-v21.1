
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import model_user

from flask import flash, session


class Magazine:

    def __init__(self, data):
        self.id = data['id']
        self.title = data["title"]
        self.description = data["description"]
        self.User_id = data["User_id"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#==================  Create ===========================

    @classmethod
    def create(cls, data:dict) ->int:
        query = "INSERT INTO magazines (title, description, user_id) VALUES (%(title)s,%(description)s, %(user_id)s);"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

# ===================  GET ONE  =======================

    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "Select * From magazines WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])

# ===================  GET ALL  =======================

    @classmethod
    def get_all(cls) -> list:
        query = "Select * From magazines:"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return False

# ===================  UPDATE ONE  =======================

    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE magazines SET title = %(title)s, description = %(description)s, WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

# =====================  DELETE  =======================

    @classmethod
    def delete_one(cls,data:dict) -> None:
        query = "DELETE FROM magazines WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

# =====================  GET ALL WITH USERS  =======================

    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * FROM magazines JOIN users ON magazines.User_id = users.id;"

        result = connectToMySQL(DATABASE).query_db(query)
        list_magazines = []
        
        for row in result:
            current_magazines = cls (row)
            user_data = {
                **row,
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"],
                "id" : row["users.id"]
            }
            current_user = model_user.User(user_data)
            current_magazines.user = (current_user)
            list_magazines.append(current_magazines)
        return list_magazines

#================== GET ONE BY USER ====================

    @classmethod
    def get_one_with_user(cls,data):
        query = "Select * FROM magazines JOIN users on magazines.User_id = users.id WHERE magazines.id = %(id)s"

        result = connectToMySQL(DATABASE).query_db(query,data)

        if len(result) > 0:
            current_magazines = cls(result[0])
            user_data = {
                **result[0],
                    "created_at" : result[0]["users.created_at"],
                    "updated_at" : result[0]["users.updated_at"],
                    "id" : result[0]["users.id"]
            }
            current_magazines.user = model_user.User(user_data)
            return current_magazines
        else:
            return None

    @staticmethod
    def validate_mag(data):
        is_valid = True

        if data['title'] == "":
            flash("title can not be empty.","err_rec_name")
            is_valid = False
        if data["description"] == "":
            flash("Desctription can not be empty.","err_rec_description")
            is_valid = False
        if data["instruction"] == "":
            flash("Instructions can not be empty.","err_rec_instruction")
            is_valid = False


        if len(data["title"]) < 3:
            flash("Title must be at least 3 characters long", "err_rec_name")
        if len(data["description"]) < 3:
            flash("Desctription must be at least 3 characters long.","err_rec_description")
            is_valid = False

        return is_valid