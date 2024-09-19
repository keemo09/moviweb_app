from datamanager.db import db

# association between user and movie
user_movie_association = db.Table(
    "user_movie",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("movie_id", db.Integer, db.ForeignKey("movies.id"), primary_key=True),
)
