
from flask import Flask,render_template,request,redirect
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

dasedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dasedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(100))

    books = db.relationship('Book', backref='my_author', lazy='dynamic')


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), unique=True)
    date = db.Column(db.DateTime)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True,)

book_publish_info = db.Table(
    'book_publish_info',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('publisher.id'), primary_key=True)
)


migrate = Migrate(app,db=db)

if __name__ == "__main__":
    app.run(debug=True,threaded = True)