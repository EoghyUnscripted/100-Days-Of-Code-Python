# Day 69 Blog Project - Adding Users

## Overview

For Day 69, we will be building our blog with the ability to allow users to register.

## Project: Adding Users

For this project, we will be allowing users to register and comment blog posts, but only the admin will be able to modify, delete or create posts.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
3. Install [SQLite Browser](https://sqlitebrowser.org/dl/)
4. Install [Flask Login](https://pypi.org/project/Flask-Login/)
5. Install [Flask Gravatar](https://pypi.org/project/Flask-Gravatar/)

### Instructions

#### Python Code

1. In `server.py`
   1. Create a `User` class and load_user function
      1. Include UserMixin, id, email, password, and name
   2. Create a `Comment` class
      1. Include id, author, text
   3. With User and Comment:
      1. Create one-to-many relational links to the `BlogPost` class
         1. Each Blog post should link to the user that created it
         2. Each comment should link to the user that created it and the blog post
         3. Each user should link to the blog posts they posted
   4. Create an `@admin_only` decorator
      1. Should check if user has id of 1 to allow admin functions like add, edit, delete posts
   5. Add the `@login_required` decorator to:
      1. logout()
      2. add_new_post()
      3. edit_post()
      4. delete_post()
   6. Build the `register()` route
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
            5. Redirect to "index.html"
   7. Build the `login()` route
      1. Allow 'GET' method:
         1. If user not authenticated, load the login form
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
   8. Create a `load_user()` route
      1. Use the `LoginManager()` decorator function to load user
      2. Pass the user id into the route function
      3. Return the database record for the user
   9. Build the `show_post()` route
      1. Allow 'GET' method:
         1. Get the requested post data from table
         2. Pass the comment form
         3. Render "post.html"
      2. Allow 'POST' method:
         1. Require users to be logged in to add comments
         2. Add comment to the database table
         3. Render the post page to show new comments
   10. Build the `logout()` route
       1. Use `logout_user()` function
       2. Render "login.html"
   11. Create the gravatar to use for default comment images
2. In `forms.py`
    1. Create forms for:
        1. RegisterForm()
        2. LoginForm()
        3. CommentForm()

#### HTML

   1. In "base.html"
      1. If user is authenticated:
         1. Hide the "register" and "login" links on nav bar
   2. In "index.html"
      1. Add jinja template to hide delete button if user not admin
   3. In "login.html"
      1. Create a `<p>` element to display flash messages
   4. In "post.html"
      1. Add the jinja templating to render all comments and gravatar icons

### Comments

This module was much more difficult to understand because we were asked to move into creating relational links (foreign keys). We have not covered this part, yet. The documentation showed us what we needed, but little for explanation.

I think the confusion came from the way it was worded in the course. For example, the course material stated that we wouldn't change the columns, which was necessary to build the relationship links.

As someone that understands relational databases, this could have been much easier.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) - Documentation for Flask SQLAlchemy
- [Flask SQLAlchemy - ORM, One-to-many](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-many)
- [Flask Login](https://flask-login.readthedocs.io/en/latest/#configuring-your-application) - Documentation for the flask_login module
