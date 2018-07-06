import os

from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

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
    #SELECT * FROM books WHERE isbn LIKE '%jerry%' OR UPPER(title) LIKE UPPER('%Ste%')
    return query
