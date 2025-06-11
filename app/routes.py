from flask import render_template, request, redirect, url_for
from . import db
from .models import Task
from flask import current_app as app

@app.route("/")
def index():
    tasks = Task.query.all()
    pending = [t for t in tasks if not t.completed]
    completed = [t for t in tasks if t.completed]
    style = app.config.get("style", {})
    return render_template("index.html", pending=pending, completed=completed, style=style)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("task_name")
    if name:
        task = Task(name=name)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.get(task_id)
    if task and not task.locked:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))
