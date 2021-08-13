from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# CREATE DATABASE
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db" <-- to create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-database.db'
db = SQLAlchemy(app)


# CREATE TABLE
# create book table using SQL alchemy
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(250), unique=True, nullable=False)
    book_author = db.Column(db.String(250), nullable=False)
    book_rating = db.Column(db.String(250), nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', book_list=all_books)


@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/form-entry", methods=['POST', 'GET'])
def receive_form_data():
    if request.method == "POST":
        form_data = request.form
        book_name = form_data['bookName']
        book_author = form_data['bookAuthor']
        book_rating = form_data['bookRating']

        # add to database Book table
        new_book = Book(book_name=book_name, book_author=book_author, book_rating=book_rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit/<int:book_id>', methods=["POST", "GET"])
def edit(book_id):
    if request.method == "POST":
        form_data = request.form
        book_to_update = Book.query.get(book_id)
        book_to_update.book_rating = form_data['editSelectedRating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html')


@app.route('/delete/<int:book_id>')
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
