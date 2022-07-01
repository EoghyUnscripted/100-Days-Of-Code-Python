# Day 57 Blog Project - Templating with Jinja in Flask

## Overview

For Day 57, we will advance into dynamic templating using Jinja in Flask.

## Project: Higher or Lower

For this project we will be creating a fake blog using JSON data and templating with Jinja to display the content on the HTML pages.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)

### Instructions

1. Get the API url from [n:Fake Blogs("https://www.npoint.io/docs/c790b4d5cab58020d391")
2. Create an HTML request and get the JSON data
   1. Loop through the data and create Post object using a class
   2. Add each to a list in the `server.py` file
3. Create a new Flask app
4. Build an index url path to an `index.html` template
   1. The index.hmtl file should be written to show all blog posts with a link to the full blog post
5. Build a blog post url path to a `blog.html` template
   1. The blog.html file should show the full blog post content of the passed blog post id
6. Include the provided CSS file in the project

### Comments

This project was fairly simple as far as completing since I have background experience in Django, which was very similar to Jinja. The most confusing part was having to use a class for the posts.

If I were to do this on my own, I would have skipped this part and simply passed the requested post id into the url function and returned the post content.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
