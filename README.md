# backend
my backend projects
## Task Manager

This is a simple task manager web application built using the Flask web framework. It allows you to add and delete tasks, and displays a list of all current tasks.

### Running the Application

To run the application, you'll need Python and Flask installed. Once you have those, do the following:

1. Open a terminal window and navigate to the directory containing the two files: `app.py` and `index.html`.
2. Run the command `flask run` to start the Flask development server.
3. Open a web browser and go to `http://localhost:5000/` to view the app.

### How it Works

The application has two parts: a `Flask` backend (`app.py`) and an HTML frontend (`index.html`).

The Flask backend uses the `Flask` class from the `flask` module to create a new Flask application instance. It defines three routes:

- `/`: The home page route. This route renders the `index.html` template and passes in a dictionary of all current tasks.
- `/add_task`: This route is triggered when the user submits the add task form on the home page. It adds a new task to the `tasks` dictionary and redirects back to the home page.
- `/delete_task/<task_id>`: This route is triggered when the user clicks the delete link next to a task. It removes the specified task from the `tasks` dictionary and redirects back to the home page.

The HTML frontend is a basic template that renders all current tasks in a list, along with a form to add new tasks. When the user submits the form, the app sends a POST request to the `/add_task` route to add the new task.

### Styling

The `index.html` file also includes some basic CSS styles to make the app look more visually appealing.
