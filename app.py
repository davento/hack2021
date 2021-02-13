from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost:5432/hack2021"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class my_user_model(db.Model):
    __tablename__ = 'my_user'
    firstname = db.Column(db.String())
    lastname  = db.Column(db.String())
    username  = db.Column(db.String(), primary_key=True)
    password  = db.Column(db.String())

    def __init__(self, firstname, lastname, username, password):
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password


@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
