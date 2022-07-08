# Day 63 SQLite and SQLAlchemy

## Overview

For Day 63, we will be learning to work with SQL and databases to store information in the Flask app.

## Project: Flask & Databases

For this project we will be using provided files and updating them to include Flask WTF forms, templating, and databases to create a book library.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask WTF Forms](https://pypi.org/project/WTForms/)
3. Install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
4. Install [SQLite Browser](https://sqlitebrowser.org/dl/)

### Instructions

1. In `server.py`:
   1. Import the `sqlite3` module
   2. Import the `flask_sqlalchemy` module
   3. Using SQLite:
      1. Create a new database called `new-books-collection.db`
      2. Create a new table called `books` with fields:
         1. id - PRIMARY KEY
         2. title - varchar(250) NOT NULL UNIQUE
         3. author - varchar(250) NOT NULL
         4. rating - FLOAT NOT NULL
   4. Using SQLAlchemy:
      1. Create a new entry
         1. id: 1
         2. title: "Harry Potter"
         3. author: "J.K. Rowling"
         4. rating: 9.3
   5. Build the `add()` function to:
      1. Accept 'POST' and 'GET' methods
      2. If 'POST':
         1. Take the form data from the `add.html` page and add it to the database
         2. Redirect to `index.hmtl`
      3. If 'GET':
         1. Load the form for users to add books
   6. Create an `edit()` function:
      1. Allow 'GET' and 'POST' methods
      2. Write the URL path to accept table id number
      3. If 'GET':
         1. Get the record from the database and pass to HTML
      4. If 'POST':
         1. Update the record in the database
         2. Redirect to `index.html`
   7. Create a `delete()` function:
      1. Allow 'POST' methods
      2. Write the URL path to accept table id number
         1. Delete the record in the database
         2. Redirect to `index.html`
2. In `index.html`:
   1. Update the code to check for records in the database
      1. If none:
         1. Display "Library is empty."
      2. Else:
         1. List the books as "Title - Author - Rating"
   2. Update the links for Flask URL parser
3. In `add.html`:
   1. Update the links for Flask URL parser
4. Create an `edit.html` template
   1. Get the database record by id
   2. Add an input field to let user update rating
   3. When submitted, update database record

### Comments

This project was a bit more difficult as it required using documentation to build it rather than tutorial to guide us. For example, with Flask, I initially figured it would be the correct way to pass the object id to the `edit()` and `delete()` paths and use that to get the record from the database.

But it wouldn't allow me to pass it and kept giving me a URL error saying that the type was wrong. I imagine being an object, this caused issues.

The argument passed had to be called through the requests module and used that way, instead. Bit confusing and will need to do some more studying to understand the logic.

#### Forking

If forking the app, please update the `server.py` details and setup your environment configurations for `secret_key`.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/#) - Documentation for WTForms
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) - Documentation for Flask SQLAlchemy
