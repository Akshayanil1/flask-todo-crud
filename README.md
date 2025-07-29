# Flask To-Do CRUD App

Live Demo: https://akshayanil15.pythonanywhere.com/

## Features
- Add, update, and delete tasks
- SQLite database
- Simple UI

## Run Locally
```bash
git clone https://github.com/Akshayanil1/flask-todo-crud.git
cd flask-todo-crud
python -m venv evenv
source evenv/bin/activate  # Linux/Mac
evenv\Scripts\activate    # Windows
pip install -r requirements.txt
python -c "from app import app, db; with app.app_context(): db.create_all()"
python app.py