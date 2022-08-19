
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import model_user

from flask import flash, session


class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.cooked_date = data["cooked_date"]
        self.under_30 = data["under_30"]
        self.User_id = data["User_id"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#==================  Create ===========================

    @classmethod
    def create(cls, data:dict) ->int:
        query = "INSERT INTO recipes (name, description, instruction, cooked_date, under_30, user_id) VALUES (%(name)s,%(description)s,%(instruction)s,%(cooked_date)s, %(under_30)s, %(user_id)s);"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

# ===================  GET ONE  =======================

    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "Select * From recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])

# ===================  GET ALL  =======================

    @classmethod
    def get_all(cls) -> list:
        query = "Select * From recipes:"
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
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, cooked_date = %(cooked_date)s,under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

# =====================  DELETE  =======================

    @classmethod
    def delete_one(cls,data:dict) -> None:
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

# =====================  GET ALL WITH USERS  =======================

    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.User_id = users.id;"

        result = connectToMySQL(DATABASE).query_db(query)
        list_recipes = []
        
        for row in result:
            current_recipe = cls (row)
            user_data = {
                **row,
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"],
                "id" : row["users.id"]
            }
            current_user = model_user.User(user_data)
            current_recipe.user = (current_user)
            list_recipes.append(current_recipe)
        return list_recipes

#================== GET ONE BY USER ====================

    @classmethod
    def get_one_with_user(cls,data):
        query = "Select * FROM recipes JOIN users on recipes.User_id = users.id WHERE recipes.id = %(id)s"

        result = connectToMySQL(DATABASE).query_db(query,data)

        if len(result) > 0:
            current_recipe = cls(result[0])
            user_data = {
                **result[0],
                    "created_at" : result[0]["users.created_at"],
                    "updated_at" : result[0]["users.updated_at"],
                    "id" : result[0]["users.id"]
            }
            current_recipe.user = model_user.User(user_data)
            return current_recipe
        else:
            return None

    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if data['name'] == "":
            flash("Name can not be empty.","err_rec_name")
            is_valid = False
        if data["description"] == "":
            flash("Desctription can not be empty.","err_rec_description")
            is_valid = False
        if data["instruction"] == "":
            flash("Instructions can not be empty.","err_rec_instruction")
            is_valid = False
        if data["cooked_date"] == "":
            flash("Must have a date.","err_rec_cooked_date")
            is_valid = False

        if len(data["name"]) < 3:
            flash("Name must be at least 3 characters long", "err_rec_name")
        if len(data["description"]) < 3:
            flash("Desctription must be at least 3 characters long.","err_rec_description")
            is_valid = False
        if len(data["instruction"]) < 3:
            flash("Instructions must be at least 3 characters long.","err_rec_instruction")
            is_valid = False

        return is_valid