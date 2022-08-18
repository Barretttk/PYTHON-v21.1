
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app import EMAIL_REGEX

from flask import flash, session


class User:

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
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"

        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

# ===================  GET ONE  =======================

    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "Select * From users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])

# ===================  GET ALL  =======================

    @classmethod
    def get_all(cls) -> list:
        query = "Select * From users:"
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
        query = "UPDATE users SET (first_name) = %(first_name)s, last_name = %(last_name)s, email = %(email)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

# =====================  DELETE  =======================

    @classmethod
    def delete(cls,data:dict) -> None:
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

# ===================  GET ONE EMAIL ALSO VALIDATE=======================

    @classmethod
    def get_one_by_email(cls, data:dict) ->None:
        query = "Select * From users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)

        if len(results) > 0:
            existing_user = cls (results[0])
            return existing_user
        else:
            return None




# =================  REG VALIDATE  ===========================

    @staticmethod
    def validate_registration(data:dict) -> bool:
        query = "Select * From users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        is_valid = True # we assume this is true

        if len(data['first_name']) < 2:
            flash("First name needs at least 2 characters.", 'err_reg_first_name')
            is_valid = False

        if len(data['last_name']) < 2:
            flash("Last name needs at least 2 characters.", 'err_reg_last_name')
            is_valid = False

        if len(data['email']) < 1:
            is_valid = False
            flash("Field is required.", 'err_reg_email')
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email!", 'err_user_email')
            is_valid = False
        else:
            # check db to see if email already exist
            existing_user = User.get_one_by_email({'email' : data['email']})
            if existing_user:
                flash("User already exist!", 'err_reg_email')
                is_valid = False
        if len (results) >= 1:
            flash("User already exist!", 'err_reg_email')
            is_valid = False

        if len(data['password']) < 1:
            flash("Field is reqired.", 'err_reg_password')
            is_valid = False

        if len(data['confirm_pw']) < 1:
            flash("Field is reqired.", 'err_reg_confirm_pw')
            is_valid = False
        elif data['password'] != data['confirm_pw']:
            is_valid = False
            flash("Passwords do not match", 'err_reg_confirm_pw')

        return is_valid

#=======================  LOGIN VALIDATE  ======================

    @staticmethod
    def validate_login(data:dict) -> bool:
        is_valid = True # we assume this is true

        if len(data['email']) < 1:
            is_valid = False
            flash("Field is required")
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'err_user_email_login')
            is_valid = False
        else:
            #cheeck db to see if email already exist
            existing_user = User.get_one_by_email({'email' : data['email']})
            if not existing_user:
                flash("Email not found!", 'err_user_email_login')
                is_valid = False

        if len(data['password']) < 1:
            flash("Field is reqired")
            is_valid = False

        if is_valid:
            # check bcrypt
            if not bcrypt.check_password_hash(existing_user.password, data["password"]):
                flash("Invalid Credentials!", 'err_user_password_login')
                is_valid = False

                #get the id into seaion
                session['user_id'] = existing_user.id

        return is_valid
