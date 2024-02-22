from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)

class Cafe(db.Model):
    # your column definitions here
    pass

# Create a new instance of Cafe
new_cafe = Cafe(
    name="New Cafe",
    map_url="https://example.com/map",
    img_url="https://example.com/image",
    location="New York",
    seats="20",
    has_toilet=True,
    has_wifi=True,
    has_sockets=True,
    can_take_calls=True,
    coffee_price="2.50"
)

@app.route("/")
def home():
    with app.app_context():
        # Add the new_cafe instance to the session
        db.session.add(new_cafe)
        # Commit the changes
        db.session.commit()

        # Render the template with the new_cafe object
        return render_template("cafes.html", cafes=[new_cafe])

if __name__ == "__main__":
    app.run(port=5000, debug=True)