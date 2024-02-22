from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
db = SQLAlchemy(app)

class Todolist(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # new_list = {
        #     'id': 4,
        #     'task': 'reminderhool',
        # }
        #
        # todolist_entry = Todolist(id=new_list['id'], task=new_list['task'])
        # db.session.add(todolist_entry)
        # db.session.commit()
        todolist_entries = Todolist.query.all()
        @app.route("/")
        def home():
            return render_template("index.html", list=todolist_entries)


        @app.route('/add', methods=['POST'])
        def add_task():
            task = request.form.get('task')
            new_task = Todolist(id=20, task=task)
            db.session.add(new_task)
            db.session.commit()
            return render_template("index.html")
    app.run(debug=True, port=5000)



