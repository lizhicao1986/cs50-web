import os
import csv

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("books.csv")
    reader = csv.reader(f)
    next(reader, None)  # skip header
    for isbn, title, author, year in reader:
        book = Book(isbn = isbn, title = title, author = author, year = year)
        db.session.add(book)
        #print(f"Added book {title} by author {author}.")
    db.session.commit()

#     for origin, destination, duration in reader:
#         flight = Flight(origin=origin, destination=destination, duration=duration)
#         db.session.add(flight)
#         print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
#     db.session.commit()
#
if __name__ == "__main__":
    with app.app_context():
        main()
# #
#
