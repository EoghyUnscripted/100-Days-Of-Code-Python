# Day 70 Developing Web Apps With Heroku

## Overview

For Day 70, we will be deploying our blog project from day 69 with heroku.

## Project: Deployment with Heroku

For this project, we will be making some finishing touches on our blog app and converting to a postgresql database.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
3. Install [SQLite Browser](https://sqlitebrowser.org/dl/)
4. Install [Flask Login](https://pypi.org/project/Flask-Login/)
5. Install [Flask Gravatar](https://pypi.org/project/Flask-Gravatar/)
6. Install [Psycopg2](https://pypi.org/project/psycopg2/)
7. Install [Gunicorn](https://pypi.org/project/gunicorn/)
8. Sign Up with [GitHub](https://www.github.com)
9. Sign Up with [Heroku](https://www.heroku.com)

### Instructions

#### Local Changes

Not much needs to change as far as code, but we do need to set up the environment with hidden variables for use with Heroku.

1. In `main.py`
   1. Import `os`
   2. Change the `SQLALCHEMY_DATABASE_URI` variable to equal `os.environ.get("DB_URL")`
   3. Change the `SECRET_KEY` variable to equal `os.environ.get("FLASK_SECRET_KEY")`
2. Create a new file in the main directory
   1. Name it exactly as `Procfile` without an extension
   2. In the file add `web: gunicorn main:app`
3. Create a `requirements.txt` file using the terminal

   ```sha
      pip freeze > requirements.txt
   ```

#### GitHub

Your application files should be uploaded as a repo to GitHub before deploying to Heroku. Most of you should be aware of how to do this.

If not, please refer to the GitHub docs to determine the best approach you should use, such as pushing your code through your IDE like VS Code or PyCharm.

#### Heroku

This is the trickiest part, so follow these steps carefully.

1. Sign Up or log into Heroku
2. At your dashboard page, click to create a new app and give it a name
3. On the app page
   1. Click the "deploy" tab
      1. Scroll down to "deployment method"
      2. Select GitHub, follow the instructions to authorize
      3. Search for your blog repo and connect it
      4. Scroll down to "automatic deploys" and click to enable
   2. Click the "resources" tab
      1. Scroll to the "add-ons" section
      2. Search for "Heroku Postgres"
      3. Click to add and select the free option
   3. Click the "settings" tab
      1. Scroll to "config vars" and select to reveal
      2. Click to edit the "DATABASE_URL" variable and copy the key
         1. Close the menu by clicking cancel
      3. Create a new key as "DB_URL"
         1. Paste the code you copied into the value box
         2. Change "postgres" to "postgresql"
         3. Click "add"
         4. Be sure to add your other hidden environment variables
            1. i.e. SECRET_KEY
   4. Click the "deploy" tab
      1. Scroll down to "manual deploy"
      2. Click "deploy branch"
      3. Once completed, click "view"

If you followed the steps correctly, you will see your app. If not, it will provide you with an error screen. From here you can just go into your app dashboard and locate the "more" button at the top right and view the log for the error messages.

### Comments

This project was a bit of a pain trying to deploy because it gave errors, but did not specify much other than the app crashed or failed to start. After testing different things, the steps above really did the trick.

If you continue to encounter problems, delete the `blog.db` file in your app and push the updates to GitHub. Heroku will rebuild and redeploy for you after a few minutes.

For this project, I created a new repo for the blog as I intend to continue building the app as well as make it easier to deploy to Heroku without the added content from the 100 Days of Code repo.

#### Heroku Demo

[Blog Demo](https://the-blurb.herokuapp.com)

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) - Documentation for Flask SQLAlchemy
- [Flask SQLAlchemy - ORM, One-to-many](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-many)
- [Flask Login](https://flask-login.readthedocs.io/en/latest/#configuring-your-application) - Documentation for the flask_login module
