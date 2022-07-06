# Day 60 POST Requests with Flask

## Overview

For Day 60, we will continue off of the Blog Project from day 59 and add some enhancements.

## Project: Blog Project - POST Form

For this project we will be continuing to build on our Blog Project to add contact form functionality.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)

### Instructions

1. Modify the contact form to remove the template extras
2. Add `name="input_name"` for each input on the form
3. Update the app route for `/contact.html`
   1. Allow the `GET` and `POST` methods
   2. Add code to execute when either method is called
      1. If `POST`
         1. Set the `<h1>` tag in `contact.html` to say "Successfully sent your message!"
         2. Output the submitted form data to the console
         3. Using `SMTPLIB`, send the form data via email to yourself
      2. If `GET`
         1. The page should load as normal
         2. The `<h1>` tag should remain "Contact Me"

### Comments

What I don't like about using SMTPLIB for this project is that the email is sent from your own email account.

If this were to be used as an actual blog, I would set up the page to submit the data into a PostgreSQL database which could be viewed using a framework like Django in the admin portal.

For this project, I modified some of the code from day 32 for the SMTPLIB email function to save some time.

#### Forking

If forking the app, please update the `server.py` details and setup your environment configurations for your email server and hidden variables.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
- [Bootstrap](https://getbootstrap.com) - Bootstrap documentaton
- [Codeply](https://www.codeply.com) - Great site for visualizing responsive code
