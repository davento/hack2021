from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost:5432/hack2021"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class my_user_model(db.Model):
    __tablename__ = 'my_user'
    firstname = db.Column(db.Text())
    lastname = db.Column(db.Text())
    username = db.Column(db.Text(), primary_key=True)
    password = db.Column(db.Text())

    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

class speciality_model(db.Model):
    __tablename__ = 'specialty'
    title = db.Column(db.Text(), primary_key=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"<specialty {self.title}>"

class r_user_speciality_model(db.Model):
    __tablename__ = 'r_user_specialty'
    username = db.Column(db.Text(), primary_key=True, ForeignKey('my_user.username'))
    title = db.Column(db.Text(), primary_key=True, ForeignKey('specialty.title'))

    def __init__(self, username, title):
        self.username = username
        self.title = title

    def __repr__(self):
        return f"<r_user_specialty {self.username, self.title}>"

class achivement(db.Model):
    __tablename__ = 'r_user_achivement'
    username = db.Column(db.Text(), primary_key=True)
    document = db.Column(db.LargeBinary())

    def __init__(self, username, document):
        self.username = username
        self.document = document
    
    def __repr__(self):
        return f"<achivement {username}>"

class r_user_achievement():

@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)