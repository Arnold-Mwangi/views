from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship('Book', backref='author')

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer)
    books = db.relationship('Book', backref='genre')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, unique=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable =False )
