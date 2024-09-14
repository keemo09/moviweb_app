from flask import Flask, render_template, request, redirect, url_for
from datamanager.sqlite_data_manager import SQLiteDataManager

app = Flask(__name__)
data_manager = SQLiteDataManager('moviwebapp.db')
data_manager.init_app(app)

@app.route('/')
def index():
    return "Hi"


@app.route('/users')
def list_users():
    '''
    Returns all the users and return it rendered in "users.html"
    '''
    users = data_manager.get_all_users()  #  fetches all user data from db.
    return render_template("users.html", users=users)


@app.route('/users/<int:user_id>')
def list_user_movies(user_id):
    '''
    Get user_id as url argument and fetches all movies from a user.
    '''
    try:
        user = data_manager.get_user(user_id)
        user_movies = data_manager.get_user_movies(user_id)
    except ValueError:
        return 404 
    
    return render_template("user_movie.htm", user_movies=user_movies, user=user)


@app.route('/add_user', methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        user_data = {"name": request.form.get("name")}
        data_manager.add_user(user_data)
        return redirect(url_for("index"))
    
    return render_template("user_form.html")


@app.route('/users/<int:user_id>/add_movie', methods=["GET", "POST"])
def add_movie(user_id):
    '''
    Get user_id as url parameter.
    Returns a movie_form and create a movie record and assioate it to user.
    '''
    if request.method == "POST":
        user = data_manager.get_user(user_id)
        movie_data = {"name": request.form.get("name"),
                      "director": request.form.get("director"),
                      "year": request.form.get("year"),
                      "rating": request.form.get("rating"),
                      "user_id": user.id
                      }

        # add movie record
        data_manager.add_movie(movie_data)
        return redirect(url_for("index"))

    return render_template("movie_form.html", user_id=user_id)
        

@app.route('/users/<int:user_id>/update_movie/<int:movie_id>')
def update_movie(user_id, movie_id):
    pass


@app.route('/users/<int:user_id>/delete_movie/<int:movie_id>')
def delete_movie(user_id, movie_id):
    pass


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)