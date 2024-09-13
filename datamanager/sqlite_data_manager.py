from flask_sqlalchemy import SQLAlchemy
from datamanager.data_manager_interface import DataManagerInterface
from datamanager.db import db 
from models.data_models import User, Movie




class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db_engine_uri = f'sqlite:///{db_file_name}'
        self.db = db

    def init_app(self, app):
        '''
        Get a app as argument.
        Set from the app config the db uri to db_engine_uri.
        Connect SQLalchemy to the app.
        Initilase SQLAlchemy with App.
        '''
        # Set the SQLALCHEMY_DATABASE_URI
        app.config["SQLALCHEMY_DATABASE_URI"] = self.db_engine_uri

        # Initilase SQLAlchemy with App
        self.db.init_app(app)

        # Create Database and tables
        with app.app_context():
            self.db.create_all()


    def get_all_users(self):
        '''
        Returns all the user date which is stored in db.
        '''
        users = User.query.all()
        users_name_list = [user.name for user in users]
        return users_name_list

    def get_user_movies(user_id):
        '''
        Get user_id as a parameter and fetches users movies.
        Returns all the movies from a specific user.
        '''
        user_in_db = User.query.get(user_id)
        
        if user_in_db:
            user_movies = user_in_db.movies
            user_movies_title_list = [movie.title for movie in user_movies]
            return user_movies_title_list
        
        else:
            raise ValueError("Invalid User!")

    def add_user(self, user):
        '''
        Get a user insance as argument and create a new record.
        '''
        self.db.session.add(user)
        self.db.session.commit()


    def add_movie(self, movie):
        '''
        Get a movie insance as argument and create a new record.
        '''
        self.db.session.add(movie)
        self.db.session.commit()

    def add_movie_to_user(self, user_id, movie_id):
        '''
        Get user_id and movie_id as argument.
        Link a excisting movie to a user.
        Return True if succesfull.
        '''

        movie_in_db = Movie.query.get(movie_id)
        user_in_db = User.query.get(user_id)

        # If movie_id didnt match to a movie in db raises error.
        if not movie_in_db:
            raise ValueError("Movie didnt exist")
        
        # If user_id didnt match to a user in db raises error.
        if not user_in_db:
            raise ValueError("Invalid User!")
        
        # append the move to the user
        user_in_db.movies.append(movie_in_db)
       
        # Commit changes to db
        self.db.session.commit()
        
        return True

    def update_movie(self, movie):
        '''
        Get a movie insance as argument and updates a existing movie.
        '''
        # Get a movie based on the id
        movie_in_db = Movie.query.get(movie.id)

        # If movie_id didnt match to a movie in db raises error.
        if movie_in_db:

            # Checks which fields a given and update it.
            if "name" in movie:
                movie_in_db.name = movie.name
            if "director" in movie:
                movie_in_db.director = movie.director
            if "year" in movie:
                movie_in_db.year = movie.year
            if "rating" in movie:
                movie_in_db.rating = movie.rating
            
            # Commit changes to db
            self.db.session.commit()
            return True
        
        else:
            raise ValueError("Movie not found!")


    def delete_movie(self, movie_id):
        '''
        Get a movie_id as argument and deletes a existing movie.
        '''
        # fetches movie by id 
        movie_in_db = Movie.querie.get(movie_id)

        # If movie_id didnt match to a movie in db raises error.
        if movie_in_db:
            
            # Deletes record from db
            db.session.delete(movie_in_db)
            return True
        else:
            return False





        
