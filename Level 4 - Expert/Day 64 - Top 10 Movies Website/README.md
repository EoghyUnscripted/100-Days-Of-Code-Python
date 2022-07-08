# Day 64 Top 10 Movies Website

## Overview

For Day 64, we will be learning to work with SQL and databases to store information in the Flask app and adding WTForms.

## Project: Top 10 Movies

For this project we will be using all of what we have learned to build a top 10 movies website similar to how we built our book library from Day 63.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask WTF Forms](https://pypi.org/project/WTForms/)
3. Install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
4. Install [SQLite Browser](https://sqlitebrowser.org/dl/)
5. Sign Up With [TMDB](https://www.themoviedb.org/) for an API key

### Instructions

1. In `server.py`:
   1. Create a SQL database with SQLAlchemy
   2. Create a "Movie" table:
      1. id
      2. title
      3. year
      4. description
      5. rating
      6. ranking
      7. review
      8. img_url
   3. Build the `home()` function
      1. Renders index.html
      2. Passes all records in the database to HTML
      3. Ordered by rating and ranked
   4. Build the `edit()` function
      1. Function will query movie record by id
      2. Create WTForm for user to edit
         1. Rating
         2. Review
      3. Update record with form data
      4. Redirect to `home()`
   5. Build the `delete()` function
      1. Query the database for the record
      2. Delete the record
      3. Redirect to `home()`
   6. Build the `search()` function
      1. Function will call API and pass movie title as query
      2. Passes returned data to HTML
   7. Build the `add()` function
      1. User will select an option in `select.html`
      2. Query API using the movie id from selection
      3. Add to database
      4. Redirect to `edit()` for user to add rating and review
2. In `index.html`:
   1. Write the Jinja templating code to get the movies cards to display correctly
   2. Update the links for Flask URL parser
   3. Each card should have an `update` and `delete` option and passes movie id
      1. Update - lets user update the rating and review
      2. Delete - lets user delete the records
3. In `edit.html`:
   1. Create WTForm for user to edit the record
   2. When updated in database table, redirect `home()`
4. In `add.html`:
   1. Create WTForm for user to search for a movie by title
   2. On submit, the page will refresh to `select.html`
5. In `select.html`:
   1. Create the template to list all movie titles returned from `search()` function

### Comments

This project was interesting with the addition of API usage, but a bit confusing trying to figure out where to find the correct endpoints based on the API documentation. It took a bit of research to figure out the base url and take it from there.

#### Forking

If forking the app, please update the `server.py` details and setup your environment configurations for `MOVIE_SEARCH_URL`, `MOVIE_API_KEY`, `MOVIE_DATA_URL`, and `MOVIE_POSTER_URL`.

      MOVIE_SEARCH_URL = "https://api.themoviedb.org/3/search/movie/"
      MOVIE_DATA_URL = "https://api.themoviedb.org/3/movie/"
      MOVIE_POSTER_URL = "https://image.tmdb.org/t/p/original"

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/#) - Documentation for WTForms
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) - Documentation for Flask SQLAlchemy
- [TMDB API](https://www.themoviedb.org/documentation/api) - API documentation for movie searches
- [How to Set and Get Environment Variables in Python](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5) - This is a great resource to learn how to create persistent environment variables
