# Day 59 Blog Project - Adding Styling

## Overview

For Day 59, we will be building a new blog with Bootstrap, Flask, and Jinja.

## Project: Blog Project

For this project we will be rebuilding a similar blog like the project from day 57, but adding Bootstrap to enhance the features and create a dynamic blog.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)

### Instructions

> **_NOTE:_** As there are way too many instruction steps to type, these are high-level instructions.

1. Download the bootstrap template from [Clean Blog](https://startbootstrap.com/previews/clean-blog)
2. Using what we now know about Jinja and Flask:
   1. Organize the file hierarchy to include a static and templates folder
   2. Create new HTML files for
      1. header.html - Add the `<head>` through `</nav>` section from index
      2. footer.html - Add the `<footer>` section from index
   3. Edit the files from step 2.2 to include your own content
      1. Meta data
      2. Blog name
      3. Website name
      4. Copyright year
      5. Update file paths (i.e. static, URLs)
   4. Use Flask URL to render each page and include the contents of:
      1. header.html
      2. Body content for the specific page
      3. footer.html
   5. Apply Jinja templating to correctly display the content on the pages
      1. Blog posts should pull from an API and be displayed on index.hmtl
      2. The full blog post should render on the url link to the full article

### Comments

The purpose of this project was to work with using templates to build a website. The content itself is generic for the most part, but can be modified to your liking.

I tweaked the code a bit to add my own name as author for visual.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [Bootstrap](https://getbootstrap.com) - Bootstrap documentaton
- [Codeply](https://www.codeply.com) - Great site for visualizing responsive code
