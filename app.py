from flask import Flask, render_template
from datamanager.sqlite_data_manager import SQLiteDataManager

app = Flask(__name__)
data_manager = SQLiteDataManager('moviwebapp.db')
data_manager.init_app(app)

@app.route('/')
def index():
    pass


@app.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return render_template("users.html", users=users)


@app.route('/users/<int:user_id>')
def list_user_movies(user_id):
    pass


@app.route('/add_user')
def add_user():
    pass


@app.route('/users/<int:user_id>/add_movie')
def add_movie(user_id):
    pass


@app.route('/users/<int:user_id>/update_movie/<int:movie_id>')
def update_movie(user_id, movie_id):
    pass


@app.route('/users/<int:user_id>/delete_movie/<int:movie_id>')
def delete_movie(user_id, movie_id):
    pass


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)