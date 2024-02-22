from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)


app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///commerce.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)



class User(db.Model, UserMixin):
    __tablename__ = "Userstable"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    phone_no = db.Column(db.String, unique=True)



class Item(db.Model):
    __tablename__ = "itemtable"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    info = db.Column(db.String)

with app.app_context():
    db.create_all()



@login_manager.user_loader
def load_user(user_id):
    # Load the user from the database based on the user_id
    user = User.query.get(int(user_id))
    return user



@app.route("/newuser", methods=["POST"])
def new():
    # Handle new user registration
    password = request.form.get("password")
    # Create a new user object
    new_user = User(
        name=request.form.get("name"),
        email=request.form.get("email"),
        phone_no=request.form.get("phone_no"),
        password=generate_password_hash(password, salt_length=8),
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("home"))




@app.route("/log", methods=["POST"])
def log():
    # Handle user login
    password = request.form.get("password")
    email = request.form.get("email")
    # Find the user by email
    user = User.query.filter_by(email=email).first()
    if not user:
        flash("You are not registered.")
        return redirect(url_for("login"))
    elif not check_password_hash(user.password, password):
        flash("Incorrect password.")
        return redirect(url_for("login"))
    else:
        login_user(user)
        return redirect(url_for("page"))

@app.route("/")
def home():
    # Render the home page
    return render_template("landing.html")



@app.route("/login")
def login():
    # Render the login page
    return render_template("login.html")



@app.route("/register")
def register():
    # Render the registration page
    return render_template("register.html")


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact")
def contact():
    return render_template("contact.html")


@login_required
@app.route("/page")
def page():
    items = db.session.query(Item).all()
    return render_template("index.html",items=items)



@login_required
@app.route("/newitem")
def add_item():
    return render_template("newitem.html")


@login_required
@app.route("/add", methods=["POST"])
def add():
    new_item = Item(
    name=request.form.get("itemname"),
    info=request.form.get("info"),
    image_url=request.form.get("image"),
    )
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for("page"))
@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@login_required
@app.route("/buy", methods=["POST"])
def buy():
    request.form.get("name")
    return redirect(url_for("page"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)