from flask_app.config.mysqlconnection import connectToMySQL


class Friend:
    db = "friend_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.occupation = data["occupation"]
        self.age = data['age']

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)
        # to show reults in termninal-------------
        print(results)
        # Create an empty list to append our instances of friends
        all_friends = []
        # Iterate over the db results and create instances of friends with cls.
        for dict in results:
            all_friends .append(cls(dict))
        return all_friends

    @classmethod
    def get_one_friend(cls,data):
            query = "SELECT * FROM friends WHERE id =%(friend_id)s;"
            results = connectToMySQL(cls.db).query_db(query, data)
            return cls(results[0])

    @classmethod
    def create_new_friend(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, age, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(occupation)s,%(age)s,NOW(),NOW());"
        results = connectToMySQL("friend_schema").query_db(query, data)
        return results