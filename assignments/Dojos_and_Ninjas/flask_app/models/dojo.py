from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from .ninja import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data["name"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

# Show all DOJOS + create DOJO


    @classmethod
    def show_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_dojos = []
        for dict in results:
            all_dojos .append(cls(dict))
        return all_dojos

# create New Dojo

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES %(name)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id =%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def showboth(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            n = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row ["last_name"],
                "age" : row ["age"],
                "created_at" : row ["ninjas.created_at"],
                "updated_at" : row ["updated_at"]
            }
            dojo.ninjas.append(Ninja(n))
        return dojo