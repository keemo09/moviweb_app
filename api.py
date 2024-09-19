from flask import Blueprint, jsonify, request
from datamanager.sqlite_data_manager import SQLiteDataManager

api = Blueprint("api", __name__)
data_manager = SQLiteDataManager("moviwebapp.db")


@api.route("/users", methods=["GET"])
def get_users():
    """
    Returns all the users and return it rendered in "users.html"
    """
    print("hi")
    users = data_manager.get_all_users()  #  fetches all user data from db.
    user_names = [user.name for user in users]
    return jsonify(user_names)


@api.route("/users/<user_id>/movies", methods=["GET"])
def list_user_movies(user_id):
    """
    Get user_id as url argument and fetches all movies from a user.
    """
    try:
        user = data_manager.get_user(user_id)
        user_movies = data_manager.get_user_movies(user_id)
        user_movies_names = [movie.name for movie in user_movies]
    except ValueError:
        response = {
            "error": "Bad Request",
            "message": f"{user_id} is not assioated to a valid user.",
        }
        return response, 404

    return jsonify(user_movies_names)


@api.route("/users/<user_id>/movies", methods=["POST"])
def add_movie(user_id):
    """
    Get user_id as url parameter.
    Returns a movie_form and create a movie record and assioate it to user.
    """
    try:
        user = data_manager.get_user(user_id)
        json_movie_data = request.get_json()
        movie_data = {
            "name": json_movie_data["name"],
            "director": json_movie_data["director"],
            "year": json_movie_data["year"],
            "rating": json_movie_data["rating"],
            "user_id": user.id,
        }

        # add movie record
        data_manager.add_movie(movie_data)
        response = {"message": "Movie added successfully"}
        return response, 202

    except ValueError:
        response = {
            "error": "Bad Request",
            "message": f"{user_id} is not assioated to a valid user.",
        }
        return response, 404
