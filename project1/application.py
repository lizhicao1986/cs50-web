import os
from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests



app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET", 'POST'])
def index():
    #return "Project 1: TODO"
    # if session['userid'] != None:
    #     return render_template("index.html", userid=session['userid'])
    return render_template("index.html", userid=session['userid'])

@app.route("/register")
def register():
    """Registration page."""
    return render_template("register.html")

@app.route("/register_account", methods=["POST"])
def register_account():
    """Register an account."""
    # Get form information.
    username = request.form.get("username")
    password = request.form.get("InputPassword")

    # Make sure username is not taken
    if db.execute("SELECT * FROM users WHERE username = :username", {'username': username}).rowcount != 0:
        return render_template("error.html", message="username already exists.")

    db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
            {'username': username, 'password': password})
    db.commit()
    return render_template("success.html")

@app.route("/login")
def login():
    """Login page."""
    return render_template("login.html")

@app.route("/login_account", methods=["POST"])
def login_account():
    # Get form information.
    username = request.form.get("username")
    password = request.form.get("InputPassword")

    if db.execute("SELECT * FROM users WHERE username = :username AND password = :password", {'username': username, 'password':password}).rowcount != 0:
        # match, log user in # get user id
        userid = db.execute("SELECT id FROM users WHERE username = :username", {'username':username}).fetchone()
        session['userid'] = userid[0]
        #return render_template("index.html",userid=session['userid'])
        return redirect(url_for('search'))

    render_template("error.html", message="could not login")

@app.route("/logout")
def logout():
    session['userid'] = None
    return render_template("index.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/search_query", methods=["POST"])
def search_query():
    query = request.form.get("query")
    query = '%'+query+'%'
    query = query.upper()
    books = db.execute("SELECT * FROM books WHERE isbn LIKE :query OR UPPER(title) LIKE :query OR UPPER(author) LIKE :query ORDER BY year DESC", {'query':query})
    num_results = db.execute("SELECT COUNT(id) FROM books WHERE isbn LIKE :query OR UPPER(title) LIKE :query OR UPPER(author) LIKE :query", {'query':query}).fetchall()
    return render_template("display_search_results.html", books=books, num_results = num_results[0][0])

@app.route("/books")
def books():
    """Lists all books."""
    books = db.execute("SELECT * FROM books").fetchmany(50)
    return render_template("books.html", books=books)

@app.route("/books/<int:book_id>")
def book(book_id):
    """Lists details about a specific book."""
    # Make sure book exists.
    book = db.execute("SELECT * FROM books WHERE id = :id", {"id": book_id}).fetchone()
    if book is None:
        return render_template("error.html", message="No such book.")

    # API key for calls to goodreads
    KEY = "Xzvu8seibhnnOnte3SaU0g"
    secret = "xEuuNsnZlphwPslb0kfjIENXXfAlSQIjOswXZqoK38M"
    isbn = book.isbn
    #isbn = db.execute("SELECT isbn from books WHERE id ")
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": "9781632168146"})
    #print(res.json())

    # get user reviews for book, if any
    reviews = db.execute("SELECT * FROM reviews WHERE isbn = :isbn", {"isbn":book.isbn}).fetchall()
    if reviews is not None:
        avg_score = db.execute("SELECT AVG(score) FROM reviews WHERE isbn = :isbn", {"isbn":book.isbn}).fetchall()
        num_reviews = db.execute("SELECT COUNT(*) FROM reviews WHERE isbn = :isbn", {"isbn":book.isbn}).fetchall()
        print(num_reviews[0][0])
        print(avg_score[0][0])

    return render_template("book.html", book=book, reviews=reviews, num_reviews=num_reviews[0][0], avg_score=avg_score[0][0])

@app.route("/add_review", methods=["POST"])
def add_review():
    # get information from form
    ISBN = request.form.get("ISBN")
    score = request.form.get("FormControlSelect")
    review_text = request.form.get("review_text")

    # make sure user has not already reviewed this book
    # run query against session["userid"] and isbn in reviews table
    # if db.execute("SELECT * FROM users WHERE username = :username AND password = :password", {'username': username, 'password':password}).rowcount != 0:
    if db.execute("SELECT * FROM reviews WHERE isbn = :isbn AND reviewer_id = :reviewer_id", {'isbn': ISBN, 'reviewer_id': str(session['userid'])}).rowcount != 0:
        return render_template("error.html", message="you have already reviewed this book.")

    db.execute("INSERT INTO reviews (reviewer_id, isbn, score, review_text) VALUES (:reviewer_id, :isbn, :score, :review_text)",
            {'reviewer_id': session['userid'], 'isbn': ISBN, 'score': score, 'review_text': review_text})
    db.commit()
    return redirect(url_for('books'))

# res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": "9781632168146"})
# print(res.json())
# {'books': [{
#                 'id': 29207858,
#                 'isbn': '1632168146',
#                 'isbn13': '9781632168146',
#                 'ratings_count': 0,
#                 'reviews_count': 1,
#                 'text_reviews_count': 0,
#                 'work_ratings_count': 26,
#                 'work_reviews_count': 113,
#                 'work_text_reviews_count': 10,
#                 'average_rating': '4.04'
#             }]
# }
