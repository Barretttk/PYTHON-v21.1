from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Authors:


    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]




    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%name)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

#         @classmethod
#     def

#         @classmethod
#     def

#         @classmethod
#     def
