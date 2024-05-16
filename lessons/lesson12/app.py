from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
load_dotenv()
my_app = Flask(__name__)
import os
print(os.getenv("key"))

class Book:
    def __init__(self, title, author, year, genre, pages):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, genre='{self.genre}', pages={self.pages})"
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "pages": self.pages
        }


# Creating 10 book instances
books = [
    Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 281),
    Book("1984", "George Orwell", 1960, "Dystopian", 328),
    Book("Moby Dick", "Herman Melville", 1851, "Adventure", 635),
    Book("Pride and Prejudice", "Jane Austen", 1813, "Romance", 279),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Tragedy", 180),
    Book("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225),
    Book("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction", 214),
    Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310),
    Book("Brave New World", "Aldous Huxley", 1932, "Science Fiction", 268),
    Book("The Lord of the Rings", "J.R.R. Tolkien", 1960, "Fantasy", 1178),
]

@my_app.route('/',methods=['GET', 'POST'])
def get_books():
    if request.method == 'POST':
        return "You are using POST"
    elif request.method == 'GET':
        return render_template("books.html", my_books = books)


@my_app.route('/<int:year>', methods=['GET', 'POST'])
def get_books_by_year(year):
    return [book.to_dict() for book in books if book.year == year]


@my_app.route('/create',methods=['GET', 'POST'])
def create_books():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        pages = request.form['pages']

        # Create a new book instance and add it to the list
        new_book = Book(title, author, int(year), genre, int(pages))
        books.append(new_book)
        return redirect(url_for('get_books'))
    elif request.method == 'GET':
        return render_template("create.html")


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=80)
