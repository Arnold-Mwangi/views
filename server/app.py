from flask_migrate import Migrate
from models import db, Author, Book, Genre
from flask import Flask, redirect, url_for, request, render_template, jsonify


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return f'<h1>Welcome to Books<h1>'

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form('title')
        genre_id = request.form('genre_id')
        author_id = request.form(author_id)

        book = Book(title=title, author_id=author_id, genre_id=genre_id)

        db.session.add(book)
        db.session.commit()
        new_book = book.id

        return redirect(url_for('sucess', book_id=new_book))
    else:
        return render_template('add_book.html')




















# @app.route('/')
# def index():
#     return f'<h1>Welcome to our Book store</h1>'

# @app.route('/add_book', methods=['GET', 'POST'])
# def add_book():
#     if request.method == 'POST':
#         title = request.form['title']
#         author_id = request.form['author_id']
#         genre_id = request.form['genre_id']

#         book = Book(title=title, author_id=author_id, genre_id=genre_id)
#         db.session.add(book)
#         db.session.commit()
#         new_book = book.id

#         return redirect(url_for('success', book_id = new_book))
#     else:
#         return render_template('add_book.html')

# @app.route('/success/<int:book_id>')
# def success(book_id):
#     book = Book.query.get(book_id)
#     if book:
#         return render_template('success.html', book = book)
#     else:
#         return render_template('not_found.html'), 404


# @app.route('/books_authors', methods=['GET'])
# def books_authors():
#     books = Book.query.all()
#     book_list = [{'title':book.title, 'author':book.author.name} for book in books]
#     return jsonify({'books': book_list})
if __name__ == '__main__':
    app.run(port=5555, debug=True)