from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__ (self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.location = db_data['location']
        self.language = db_data['language']
        self.comment = db_data['comment']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return Dojo(results[0])

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) <3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) <1:
            flash("A location must be specified.")
            is_valid = False
        if len(dojo['language']) <1:
            flash("A language must be specified.")
            is_valid = False
        if len(dojo['comment']) < 5:
            flash("Comments cannot be shorter than 5 characters long.")
            is_valid = False
        return is_valid