from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        # self.dojos_id = dojo["dojo_id"]

    # @classmethod
    # def show_all_ninjas(cls):
    #     query = "SELECT * FROM ninjas;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     print(results)
    #     all_ninjas = []
    #     for dict in results:
    #         all_ninjas .append(cls(dict))
    #     return all_ninjas

# create New Ninja

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def showdojo(cls, data):
        query = "SELECT * FROM users WHERE id =%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
