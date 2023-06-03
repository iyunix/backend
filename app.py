# import necessary lib
from flask import Flask, request, jsonify, g
from datetime import datetime
import mysql.connector

# create web application
app = Flask(__name__)

# create a connection to the MySQL database
config = {
    'user': 'i_yunu3',
    'password': 'A.g.0720831717',
    'host': 'localhost',
    'database': 'mydb',
}
cnx = mysql.connector.connect(**config)

def get_db():
    return cnx

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# initialize database
with app.app_context():
    cursor = cnx.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTO_INCREMENT, content TEXT, time DATE)''')

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
            cursor = get_db().cursor()
            cursor.execute("INSERT INTO entries (content, time) VALUES (%s, %s)", (entry_content, time))

            # commit the changes
            get_db().commit()

            return "Entry has been added!"

    return "Hello, World!"

# C'R'UD: Read
@app.route("/content")
def show_content():
    with app.app_context():
        # execute the sql code to select all data has been stored
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM entries")
        rows = cursor.fetchall()

        entries = {}

        for row in rows:
            entries[row[0]] = {"content": row[1], "time": row[2].strftime("%Y-%m-%d")}

    return jsonify(entries)

# CR'U'D: Update
@app.route("/update", methods=["PUT"])
def update_entry():
    # get the id from user
    entry_id = request.form.get("id")

    # get the content from user
    new_content = request.form.get("content")

    with app.app_context():
        # execute sql code in oeder to update the content
        cursor = get_db().cursor()
        cursor.execute("UPDATE entries SET content=%s WHERE id=%s", (new_content, entry_id))
        get_db().commit()

    return "Entry has been updated!"

@app.route("/delete",methods=["DELETE"])
def del_entry():
    entry_id = request.form.get("id")

    with app.app_context():
        cursor = get_db().cursor()
        cursor.execute("DELETE FROM entries WHERE id=%s", (entry_id,))
        get_db().commit()

    return "Entry has been deleted!"

if __name__ == '__main__':
    app.run(port=8000)
