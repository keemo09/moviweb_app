# Movieweb_app
A web application for managing users and their movies, built with Flask and SQLite.

## Installation

1. Clone the repository:
   git clone https://github.com/keemo09/moviweb_app.git
   
2. Install dependencies:
   pip install -r requirements.txt

3. Run the application
   uvicorn app:app --reload


## **Usage**

After starting the application, open your browser and navigate to `http://127.0.0.1:5002` to access the web application or `http://127.0.0.1:5002/api` for the api

### **API Endpoints**

- **`GET /users`**: Fetch all users.
- **`GET /users/<user_id>/movies`**: Fetch all movies of a specific user by their user ID.
- **`POST /users/<user_id>/movies`**: Add a new movie for a specific user.
- **Request Body Example**:
    ```json
    {
        "name": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "rating": 8.8
    }
    ```
- **`GET /book/<int:book_id>`**: Fetch the details of a specific book by ID.
- **`GET /author/<int:author_id>`**: Fetch the details of a specific author by ID.
- **`POST /book/<int:book_id>/delete`**: Delete a book by its ID.


## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).




## Contact

Created by [keemo09](https://github.com/keemo09) - feel free to reach out!
