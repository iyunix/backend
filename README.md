Flask Web Application with SQLite Database

This is a simple Flask web application that uses SQLite database to store and manage user entries. The application has CRUD functionality where the user can create, read, update, and delete their entries.
Prerequisites

To run this application, you need to have Python 3.x installed on your machine. You also need to install the following dependencies:

    flask
    sqlite3

You can install these dependencies using pip. For example:

pip install flask sqlite3

Running the Application

    Clone this repository or download the source code.
    Open a terminal in the project root directory.
    Run the following command to start the application:

python app.py

    Open a web browser and go to http://localhost:8000/ to access the application.

Functionality

The application provides the following functionality:

    Create: Add a new entry to the database by sending a POST request to the home route ("/") with the entry content in JSON format.
    Read: View all entries in the database by sending a GET request to the "/content" route. The response will be in JSON format.
    Update: Update an existing entry in the database by sending a POST request to the "/update" route with the entry ID and new content in form data.
    Delete: Delete an existing entry from the database by sending a POST request to the "/delete" route with the entry ID in form data.

Database

The application uses a SQLite database to store and manage user entries. The database schema consists of a table named "entries" with three columns:

    id (INTEGER): Primary key that auto-increments for each new entry.
    content (TEXT): Textual content of the entry.
    time (TEXT): Date and time when the entry was created.
