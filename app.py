from flask import Flask
from datamanager.sqlite_data_manager import SQLiteDataManager

app = Flask(__name__)
data_manager = SQLiteDataManager('moviwebapp.db')
data_manager.init_app(app)

@app.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return str(users)  # Temporarily returning users as a string

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)