# Day 68 Authentication with Flask

## Overview

For Day 68, we will be moving into user authentication for logging in, out, and restricting certain page views.

## Project: User Authentication

For this project, we will be using a base template and adding the functionality for user authentication.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
3. Install [SQLite Browser](https://sqlitebrowser.org/dl/)
4. Install [Flask Login](https://pypi.org/project/Flask-Login/)

### Instructions

1. In `server.py`
   1. Build the `home()` route
      1. Check if user is logged in
      2. Render the "index.html" page
   2. Build the `register()` route
      1. Allow 'GET' method:
         1. If user not authenticated, load the registration form
      2. Allow 'POST' method:
         1. Write boolean that checks for existing user email
         2. If exists:
            1. Redirect to login page
            2. Flash message to state user exists
         3. If does not exist:
            1. Hash and salt the password
            2. Create a new user object and pass form data
            3. Add to database
            4. Authenticate the user
            5. Redirect to "secrets.html"
   3. Build the `login()` route
      1. Allow 'GET' method:
         1. If user not authenticated, load the login form
         2. If user authenticated, redirect to "secrets.html"
      2. Allow 'POST' method:
         1. Write boolean that checks credentials
         2. If exists and matches:
            1. Authenticate the user
            2. Redirect to "secrets.html"
         3. If email does not exist:
            1. Flash message to state invalid email
            2. Reload login form
         4. If password incorrect:
            1. Flash message to state invalid password
   4. Create a `load_user()` route
      1. Use the `LoginManager()` decorator function to load user
      2. Pass the user id into the route function
      3. Return the database record for the user
   5. Build the `secrets()` route
      1. Require login to access
      2. Render "secrets.html"
      3. Pass username and auth status
   6. Build the `logout()` route
      1. Use `logout_user()` function
      2. Render "login.html"
   7. Build the `download()` route
      1. Require login
      2. Return `send_from_directory()` function
         1. Pass the "cheat_sheet.pdf" file
   8. In "base.html"
      1. If user is authenticated:
         1. Hide the "register" and "login" links on nav bar
   9. In "login.html"
      1. Create a `<p>` element to display flash messages

### Comments

I made some modifications to the hmtl files to extend templating. I was aiming to reduse code a little more than simply having repeated `{% block %}{% endblock %}` lines. But I ended up having to add more because of the required blocks for navigation and footer.

For example, I had to use extra blocks because I couldn't get the navigation or footer to load without block template tags added to the child pages.

I should be able to render the content on "base.html" to the child pages without using include. Which, didn't work, either. Not sure I like templating all that much except for using it with a nav bar and footer.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) - Documentation for Flask SQLAlchemy
- [Flask Login](https://flask-login.readthedocs.io/en/latest/#configuring-your-application) - Documentation for the flask_login module
