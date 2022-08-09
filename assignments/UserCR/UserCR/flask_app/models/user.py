from flask_app.config.mysqlconnection import connectToMySQL


class User:
    db = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


#====================================
# Show All Users
#====================================

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"

        # make sure to call the connectToMySQL function with the schema you are targeting.

        results = connectToMySQL(cls.db).query_db(query)

        # to show reults in termninal-------------
        print(results)

        # Create an empty list to append our instances of (name)
        all_users = []

        # Iterate over the db results and create instances of (name) with cls.
        for dict in results:

            all_users .append(cls(dict))
        return all_users

#====================================
# Create New user 
#====================================

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        results = connectToMySQL("users_schema").query_db(query, data)
        return results