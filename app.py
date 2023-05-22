from flask import Flask, request, render_template, redirect

app = Flask(__name__)

tasks = {}

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    task_description = request.form.get("description")
    id = str(len(tasks))
    tasks[id] = task_description
    return redirect("/")

@app.route("/delete_task/<task_id>", methods=["GET"])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
