from flask_sqlalchemy import SQLAlchemy
from datamanager.db import db 
from models.user_movie_mapping import user_movie_association

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    movies = db.relationship('Movie', secondary=user_movie_association, backref='users')


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    director = db.Column(db.String)
    year = db.Column(db.String)
    rating = db.Column(db.Float)
