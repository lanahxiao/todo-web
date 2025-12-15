from flask import Flask, render_template, request, redirect
import todo_core

app = Flask(__name__)

@app.route("/")
def index():
    tasks = todo_core.load_tasks()
    completed = sum(1 for t in tasks if t["completed"])
    pending = len(tasks) - completed
    return render_template(
        "index.html",
        tasks=tasks,
        completed=completed,
        pending=pending
    )

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("todo")
    if text:
        todo_core.add_task(text)
    return redirect("/")

@app.route("/toggle/<task_id>")
def toggle(task_id):
    todo_core.toggle_task(task_id)
    return redirect("/")

@app.route("/delete/<task_id>")
def delete(task_id):
    todo_core.delete_task(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",   # ⭐关键
        port=5000,
        debug=False,
        use_reloader=False
    )

