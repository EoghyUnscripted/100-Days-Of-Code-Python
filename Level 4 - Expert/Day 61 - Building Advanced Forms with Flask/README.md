# Day 61 Building Advanced Forms with Flask

## Overview

For Day 61, we will be learning how to work with advanced forms in Flask.

## Project: Flask WTForms

For this project we will be using provided files and updating them to include Flask WTF forms and template inheriting.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask WTF Forms](https://pypi.org/project/WTForms/)
3. Install [Flask Bootstrap](https://pypi.org/project/Flask-Bootstrap/)

### Instructions

1. Create a `base.html` file in templates
   1. Use Jinja templating as we learned in day 59 to create a main template
2. Update these files to extend the `base.html` template:
   1. index.html
   2. login.html
   3. denied.html
   4. success.html
3. In the `server.py` file:
   1. Import Flask Bootstrap and WTForms
   2. Create a `login()` function and app route to "/login"
      1. Use 'GET' and 'POST' methods
      2. If 'POST':
         1. Validate the incoming form data
         2. Check to match the credentials:
            1. Email = admin@email.com
            2. Password = 12345678
         3. If form data matches, route to `success.html`
         4. Else, route to `denied.html`
      3. If 'GET':
         1. Load the `login.html` and display the form
4. In the `login.html` file:
   1. Import the bootstrap wtf.html as wtf
   2. Create a `quick_form()` on the page

### Comments

This project was a little more complicated as the documentation was a bit scattered and did not show too much for references. The course also gave high-level requirements and not much for specifics.

The key to this project was figuring out the specifics such as knowing how to start a new Flask app with Bootstrap and calling it.

Otherwise, I was able to put it all together using background with Django to manage the templating and getting the app to function correctly.

#### Forking

If forking the app, please update the `server.py` details and setup your environment configurations for `secret_key`.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/#) - Documentation for WTForms
- [Flask Bootstrap](https://bootstrap-flask.readthedocs.io/en/stable/) - Documentation for Bootstrap with Flask
