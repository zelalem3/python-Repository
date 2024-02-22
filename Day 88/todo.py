from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///do.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)


@app.route("/")
def home():
    todolist_entries = Task.query.all()
    return render_template("index.html", list=todolist_entries)


@app.route('/add', methods=['POST'])
def add_task():

    task = request.form.get('task')
    new_task = Task(description=task)
    db.session.add(new_task)
    db.session.commit()
    todolist_entries = Task.query.all()

    return render_template("index.html", list=todolist_entries)


@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("value")
    if id:
        task = db.session.query(Task).get(id)
        if task:
            db.session.delete(task)
            db.session.commit()
        else:
            print("Task not found with th id of :", id)
    else:
        print("No value received in form data")

    todolist_entries = Task.query.all()
    return render_template("index.html", list=todolist_entries)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5000)