from flask_sqlalchemy import SQLAlchemy
from data_manager_interface import DataManagerInterface

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db = db
        self.db_engine_uri = f'sqlite:///{db_file_name}'

    def init_app(self, app):
        # Set the SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_DATABASE_URI"] = self.db_engine_uri

        # Initilase SQLAlchemy with App
        self.db.init_app(app)

    def get_all_users():
        users = User.query.all()
        return users

    def get_user_movies(user_id):
        pass

    def add_user(self, user):
        self.db.session.add(user)
        self.db.session.commit()


    def add_movie(self, movie):
        self.db.session.add(movie)
        self.db.session.commit()

    def update_movie(movie):
        pass

    def delete_movie(movie_id):
        pass





        
