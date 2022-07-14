# Day 67 Blog with RESTful Routing

## Overview

For Day 67, we will be drafting our blog site using RESTful routing and including WTForms for creating new blog posts.

## Project: RESTful Blog

For this project, we will be building routes that use the RESTful services to build our blog.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)
2. Install [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
3. Install [Flask CKEditor](https://pypi.org/project/Flask-CKEditor/)
4. Install [SQLite Browser](https://sqlitebrowser.org/dl/)

### Instructions

1. In `server.py`
   1. Build the `home()` route
      1. Render the "index.hmtl" page with all blog posts
   2. Build the `show_post()` route
      1. Get index from SQL table
      2. Render the "post.html" page with selected blog
   3. Create a `new_post()` route
      1. Use 'GET' and 'POST' methods
      2. On 'GET':
         1. Show the `CreatePostForm()` with WTForms
         2. "Body" - Should use the CKEditorField
      3. On 'POST':
         1. Add record to table
         2. Route to `home()` which will show new blog post in list
   4. Create a `edit_post()` route
      1. Use 'GET' and 'POST' methods
      2. On 'GET':
         1. Show the `CreatePostForm()` with WTForms, prefilled
         2. "Body" - Should use the CKEditorField
      3. On 'POST':
         1. NOTE: CKEditor only works with POST, not PATCH or PUT
         2. Add record to table
         3. Route to `home()` which will show edited blog post in list
   5. Build the `delete_post()` route
      1. Get the post index id
      2. Delete index from SQL table

### Comments

I made some modifications to the hmtl files to extend templating. I was aiming to reduse code a little more than simply having repeated `{% block %}{% endblock %}` lines. But I ended up having to add more because of the required blocks for navigation and footer.

For example, I had to use extra blocks because I couldn't get the navigation or footer to load without block template tags added to the child pages.

I should be able to render the content on "base.html" to the child pages without using include. Which, didn't work, either. Not sure I like templating all that much except for using it with a nav bar and footer.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) - Documentation for Flask SQLAlchemy
- [Flask CKEditor](https://flask-ckeditor.readthedocs.io/en/latest/) - Documentation on the CKEditor
