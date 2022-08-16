from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, session


class  User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#==================  Create ===========================

    @classmethod
    def create(cls, data:dict) ->int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s"
        return connectToMySQL("DATABASE").query_db(query, data)


# ===================  GET ONE  =======================

    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "Select * From users WHERE id = %(id)s:"
        results = connectToMySQL("DATABASE").query_db(query, data)
        if results:
            return cls(results[0])

# ===================  GET ALL  =======================

    @classmethod
    def get_all(cls) -> list:
        query = "Select * From users:"
        results = connectToMySQL("DATABASE").query_db(query)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return False

# ===================  UPDATE ONE  =======================

    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE users SET (first_name) = %(first_name)s, last_name = %(last_name)s, email = %(email)s;"
        return connectToMySQL("DATABASE").query_db(query, data)

# =================  VALIDATE  ===========================

    # @staticmethod
    # def validate(data):
    #     is_valid = True # we assume this is true
    #     if len(data['first_name']) < 0:
    #         flash("Field is Required." 'err_user_first_name')
    #         is_valid = False

    #     if len(data['Last_name']) < 0:
    #         flash("Bun must be at least 3 characters.")
    #         is_valid = False

    #     if int(data['email']) < 0:
    #         is_valid = False
    #         flash("Field is required")
    #     elif not EMAIL

    #         is_valid = False

    #     if len(data['password']) < 3:
    #         flash("Bun must be at least 3 characters.")
    #         is_valid = False

    #     return is_valid
