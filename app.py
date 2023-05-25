# import necessary lib
from flask import Flask, request, render_template, jsonify, g
from datetime import datetime
import sqlite3

# create web application
app = Flask(__name__)

DATABASE = 'entries.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# initialize database
with app.app_context():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, time TEXT)''' )

# 'C'RUD: Create
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # get entry from user
        entry_content = request.json.get("content")

        # time of the request
        time = datetime.today().strftime("%Y-%m-%d")

        with app.app_context():
            # interact with database to insert data into it
            db = get_db()
            cursor = db.cursor()
            cursor.execute("INSERT INTO entries (content, time) VALUES (?, ?)", (entry_content, time))

            # commit the changes
            db.commit()
            
            return "Entry has been added!"

    return "Invalid request"

# C'R'UD: Read
@app.route("/content")
def show_content():
    with app.app_context():
        # execute the sql code to select all data has been stored
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM entries")
        rows = cursor.fetchall()

        entries = {}

        for row in rows:
            entries[row[0]] = {"content": row[1], "time": row[2]}

    return jsonify(entries)

# CR'U'D: Update
@app.route("/update", methods=["POST"])
def update_entry():
    # get the id from user
    entry_id = request.form.get("id")

    # get the content from user
    new_content = request.form.get("content")

    with app.app_context():
        # execute sql code in oeder to update the content
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE entries SET content=? WHERE id=?", (new_content, entry_id))
        db.commit()

    return "Entry has been updated!"

@app.route("/delete",methods=["POST"])
def del_entry():
    entry_id = request.form.get("id")

    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM entries WHERE id=?", (entry_id,))
        db.commit()

    return "Entry has been deleted!"

if __name__ == '__main__':
    app.run(port=8000)
