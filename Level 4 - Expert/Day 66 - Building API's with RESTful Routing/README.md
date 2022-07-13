# Day 66 Building API's with RESTful Routing

## Overview

For Day 65, we will be focusing on routing to build an API.

## Project: Cafe & Wifi API

For this project, we will be building routes that use the RESTful services to build an API for finding cafe's.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
3. Install [SQLite Browser](https://sqlitebrowser.org/dl/)
4. Sign up with [Postman](https://www.postman.com)

### Instructions

1. In `server.py`
   1. Create a `all()` route
      1. Include 'GET' method
      2. Return all cafe records from the Cafe table
   2. Create a `random()` route
      1. Include 'GET' method
      2. Return a random Cafe from the Cafe table
   3. Create a `search()` route
      1. Include 'GET' method
      2. Accepts a location variable passed in the request
      3. Return the matching cafes in the area
      4. If none, pass a not found message
   4. Create a `new()` route
      1. Include 'POST' method
      2. Accepts the variables for the Cafe class
      3. Passes new record into the Cafe table
   5. Create a `update_price()` route
      1. Include 'PATCH' method
      2. Accepts `new_price` header variable
      3. URL should be '/update-price/<int:cafe_id>'
      4. Query the Cafe table to get the cafe by id
         1. Update the price with the new price
   6. Create a `delete()` route
      1. Include 'DELETE' method
      2. URL should be '/report-closed/<int:cafe_id>'
      3. Query the Cafe table to get the cafe by id
         1. Delete the record from the table
2. With Postman
   1. NOTE: Be sure to login on your free account before these steps or you will lose your work
   2. Create a new collection called "Cafe & Wifi"
   3. Add requests for each route we created in step 1
   4. Publish the documentation
      1. Get the URL provided
3. In `index.html`
   1. Add the documentation URL as a link on the page

### Comments

This project was interesting as it included using Postman2 to test the routes and responses. The tricky part was figuring out how to publish documentation.

For this part, you need to sign up for the account and be logged in with your desktop app. Then create your collections. It will display a button in the documentation tab to publish.

NOTE: You can use any generated API key. Be sure to update it in the `server.py` file in the `delete()` route.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) - Documentation for Flask SQLAlchemy
- [How to Set and Get Environment Variables in Python](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5) - This is a great resource to learn how to create persistent environment variables
