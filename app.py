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
    lastname  = db.Column(db.Text())
    username  = db.Column(db.Text(), primary_key=True)
    password  = db.Column(db.Text())

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
        return f"<r_user_specialty {self.username}, {self.title}>"

class achivement_model(db.Model):
    __tablename__ = 'r_user_achivement'
    title = db.Column(db.Text(), primary_key=True)
    document = db.Column(db.LargeBinary())

    def __init__(self, title, document):
        self.title = title
        self.document = document
    
    def __repr__(self):
        return f"<achivement {title}>"

class r_user_achievement_model():
    __tablename__ = 'r_user_achievement'
    username = db.Column(db.Text(), primary_key=True)
    title = db.Column(db.Text(), primary_key=True)

class dpoint_model:
    __tablename__   = "dpoint"
    id              = db.Column(db.Integer(), primary_key=True)
    fid             = db.Column(db.Integer())
    thecontent      = db.Column(db.Text())
    participation   = db.Column(db.Integer())
    totalscore      = db.Column(db.integer())

    def __init__(self, id, fid, thecontent, participation, totalscore):
        self.id              = id
        self.fid             = fid
        self.thecontent      = thecontent
        self.participation   = participation
        self.totalscore      = totalscore


class comment_model:
    __tablename__="comment"
    id          = db.Column(db.Integer(), primary_key=True)
    dpoint      = db.Column(db.Integer())
    thecontent  = db.Column(db.Text())
    likes       = db.Column(db.Integer())
    dislikes    = db.Column(db.Integer())

    def __init__(self, id, dpoint, thecontent, likes, dislikes):
        self.id          = id
        self.dpoint      = dpoint
        self.thecontent  = thecontent
        self.likes       = likes
        self.dislikes    = dislikes

class tag_model:
    __tablename__   = "tag"
    name            = db.Column(db.Text(),primary_key=True)

    def __init__(self, name):
        self.name       = name

class author_model:
    __tablename__   = "author"
    name            = db.Column(db.Text(),primary_key=True)

    def __init__(self, name):
        self.name       = name

class paper_model:
    __tablename__   = "paper"
    title       = db.Column(db.Text(), primary_key=True)
    tag         = db.Column(db.Text())
    author      = db.Column(db.Text())
    based_on    = db.Column(db.Text())
    publisher   = db.Column(db.Text())
    pubd        = db.Column(db.Date())
    pdf         = db.Column(db.LargeBinary())
    link        = db.Column(db.Text())

    def __init__(self, title, tag, author, based_on, publisher, pubd, pdf, link):
        self.title       = title
        self.tag         = tag
        self.author      = author
        self.based_on    = based_on
        self.publisher   = publisher
        self.pubd        = pubd
        self.pdf         = pdf
        self.link        = link

@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
