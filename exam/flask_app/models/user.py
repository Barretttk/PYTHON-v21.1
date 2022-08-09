from flask_app.config.mysqlconnection import connectToMySQL


class user:
    db = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_new_user(cls, data):
        query = "INSERT INTO friends (first_name, last_name, email,created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        results = connectToMySQL("users_schema").query_db(query, data)
        return results