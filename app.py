from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = \
"postgresql://postgres:password@db:5432/studentdb"

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route("/")
def home():
    return "Flask + PostgreSQL + Docker Compose 🚀 version 5 heyyy!!!!!!!"


@app.route("/add/<name>")
def add_student(name):
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()

    return f"{name} added successfully"


@app.route("/students")
def students():

    data = Student.query.all()

    result = ""

    for student in data:
        result += f"{student.id} - {student.name}<br>"

    return result


# Wait for PostgreSQL container to finish startup
time.sleep(30)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)