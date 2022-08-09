from turtle import title
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Books:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.number_of_pages = data['number_of_pages']

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


#     @classmethod
#     def

#         @classmethod
#     def

#         @classmethod
#     def

#         @classmethod
#     def
