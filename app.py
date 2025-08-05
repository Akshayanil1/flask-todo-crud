# app.py
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# --- Database Setup ---
# 1. Initialize the Flask App
app = Flask(__name__)

# 2. Configure the database.
#    'SQLALCHEMY_DATABASE_URI': This is the connection string.
#    'sqlite:///skills.db' tells SQLAlchemy to create a SQLite database
#    file named 'skills.db' in our project directory.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# 3. Create the database object. This object is our main entry point
#    for all database operations.
db = SQLAlchemy(app)

# --- Define the Data Model ---
# 4. Create a class that inherits from db.Model. This is our blueprint for the data.
#    SQLAlchemy will automatically create a table named 'Task' based on this.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # A unique ID for each task. The primary key.
    task = db.Column(db.String(200), nullable=False) # The task name, cannot be empty.
    status = db.Column(db.Boolean, default=False)

@app.route('/')  # Define the route for the homepage (root URL).
def index():  # Define the function to handle requests to the homepage.
    tasks = Task.query.all()  # Query all Task records from the database and store them in 'tasks'.
    return render_template("index.html", tasks=tasks)  # Render the 'index.html' template, passing the tasks list.

@app.route('/add', methods=['POST'])  # Define the route for adding a new task, only accepts POST requests.
def add():  # Define the function to handle adding a new task.
    task_content = request.form['task']  # Get the 'task' value from the submitted form data.
    new_task = Task(task=task_content)  # Create a new Task object with the provided task content.
    db.session.add(new_task)  # Add the new task object to the current database session.
    db.session.commit()  # Commit the session to save the new task in the database.
    return redirect(url_for('index'))  # Redirect the user back to the homepage.

@app.route('/update/<int:id>')  # Define the route for updating a task's status, expects an integer id in the URL.
def update(id):  # Define the function to handle updating a task.
    task = Task.query.get_or_404(id)  # Query the task by id, or return a 404 error if not found.
    task.status = not task.status  # Toggle the task's status (True becomes False, False becomes True).
    db.session.commit()  # Commit the change to the database.
    return redirect(url_for('index'))  # Redirect the user back to the homepage.

@app.route('/delete/<int:id>')  # Define the route for deleting a task, expects an integer id in the URL.
def delete(id):  # Define the function to handle deleting a task.
    task = Task.query.get_or_404(id)  # Query the task by id, or return a 404 error if not found.
    db.session.delete(task)  # Mark the task for deletion in the current database session.
    db.session.commit()  # Commit the deletion to the database.
    return redirect(url_for('index'))  # Redirect the user back to the homepage.

if __name__ == '__main__':  # Check if this script is being run directly (not imported).
    with app.app_context():  # Create an application context for database operations.
        db.create_all()  # Create all database tables defined by SQLAlchemy models if they don't exist.
    app.run(debug=True)  # Start the Flask development server with debug mode enabled.