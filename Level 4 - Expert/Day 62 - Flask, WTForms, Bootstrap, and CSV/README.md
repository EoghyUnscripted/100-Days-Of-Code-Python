# Day 62 Flask, WTForms, Bootstrap and CSV

## Overview

For Day 62, we will be implementing a Bootstrap Flask app using CSV data.

## Project: Flask, Bootstrap, Forms, & Data

For this project we will be using provided files and updating them to include Flask WTF forms and template inheriting along with using CSV data.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask WTF Forms](https://pypi.org/project/WTForms/)
3. Install [Flask Bootstrap](https://pypi.org/project/Flask-Bootstrap/)

### Instructions

1. In `server.py`:
   1. Build the `CafeForm` class
      1. Include the correct module fields
         1. Location - URL Field with validation
         2. Coffee Rating - Select field with options for 0-5
         3. Wifi Rating - Select field with options for 0-5
         4. Power Outlet Rating - Select field with options for 0-5
   2. Build the `add_cafe()` function
      1. The function should collect form data when adding a new cafe
      2. It should also write the data to a new line in the CSV file
2. Update the template files to extend `base.html`
3. Base file should include the custom CSS file and extend bootstrap
   1. Hint: Use block templating

### Comments

The trickiest part of this project was getting the CSS styling to push across all pages. I realized the main reason was due to the original files extending `bootstrap/base.html`. I changed all but the index page to extend just `base.html` and it properly loaded the pages with CSS styling.

#### Forking

If forking the app, please update the `server.py` details and setup your environment configurations for `secret_key`.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/#) - Documentation for WTForms
- [Flask Bootstrap](https://bootstrap-flask.readthedocs.io/en/stable/) - Documentation for Bootstrap with Flask
