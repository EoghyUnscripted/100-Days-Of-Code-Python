"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 63
PROJECT: Flask & Databases
LEVEL: Expert

"""


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Setup database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create a new table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# Create initial record
# new_book = Book(title="Harry Potter", author="J.K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


@app.route('/')
def home():
    
    all_books = db.session.query(Book).all()
    
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        
        data = request.form
    
        new_book = Book(title=data['title'], author=data['author'], rating=data['rating'])
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('home'))
        
    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    
    if request.method == "POST":
        
        book_id = request.form["id"]
        update_rating = Book.query.get(book_id)
        update_rating.rating = request.form["rating"]
        db.session.commit()
        
        return redirect(url_for('home'))
    
    book_id = request.args.get('id')
    edit_book = Book.query.get(book_id)
    
    return render_template("edit.html", book=edit_book)


@app.route("/delete", methods=['GET'])
def delete():
    
    book_id = request.args.get('id')
    
    delete_book = Book.query.get(book_id)
    db.session.delete(delete_book)
    db.session.commit()
    
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

