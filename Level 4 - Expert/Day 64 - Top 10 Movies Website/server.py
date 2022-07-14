"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 64
PROJECT: Top 10 Movies
LEVEL: Expert

"""

from django.shortcuts import render
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from decouple import config


MOVIE_SEARCH_URL = config("TMDB_SEARCH_URL")
MOVIE_API_KEY = config("TMDB_API_KEY")
MOVIE_DATA_URL = config("TMDB_MOVIE_URL")
MOVIE_POSTER_URL = config("TMDB_IMG_URL")


app = Flask(__name__)
app.config['SECRET_KEY'] = config("FLASK_SECRET_KEY")
Bootstrap(app)

# Setup database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create a new table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()


# Create initial record
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


class EditMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5',
                         validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Search')


@app.route("/")
def home():

    all_movies = Movie.query.order_by(Movie.rating).all()
    
    for i in range(len(all_movies)):
        
        all_movies[i].ranking = len(all_movies) - i
        
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/search", methods=["GET", "POST"])
def search():

    form = AddMovieForm()

    if form.validate_on_submit():

        movie_title = form.title.data
        print(movie_title)
        r = requests.get(
            f"{MOVIE_SEARCH_URL}?api_key={MOVIE_API_KEY}&query={movie_title}")
        data = r.json()['results']

        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/add")
def add():

    movie_id = request.args.get('id')
    r = requests.get(f"{MOVIE_DATA_URL}{movie_id}?api_key={MOVIE_API_KEY}")
    data = r.json()

    new_movie = Movie(
        title=data["original_title"],
        year=data["release_date"].split("-")[0],
        description=data["overview"],
        img_url=f"{MOVIE_POSTER_URL}{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():

    form = EditMovieForm()

    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)

    if form.validate_on_submit():

        movie.rating = request.form["rating"]
        movie.review = request.form["review"]
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():

    movie_id = request.args.get('id')

    delete_movie = Movie.query.get(movie_id)
    db.session.delete(delete_movie)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
