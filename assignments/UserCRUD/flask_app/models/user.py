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
# Show All Users method
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
# Create New method
#====================================

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        results = connectToMySQL("users_schema").query_db(query, data)
        return results

#====================================
# Show One method
#====================================

    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id =%(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

#====================================
# Delete one method
#====================================

    @classmethod
    def delete_one_user(cls,data):
        query = "DELETE FROM users WHERE id =%(user_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    

#====================================
# Update User method
# ===================================

    @classmethod
    def update_one_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(user_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

