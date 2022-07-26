from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from decouple import config
import smtplib


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
    

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Register')
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Passowrd', validators=[DataRequired()])
    submit = SubmitField('Log In')


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField('Add Reply')
    

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
    

def send_email(name, email, message):
    """ Function used to send email when contact form is filled out and posted. """
    
    # NOTE: For security, I have not included my credentials. You will want to fill in your own depending on your service.
    
    # Set variables
    send_from = config("GMAIL_ACCT")                    # Email address
    password = config("GMAIL_PASSWORD")                 # Email password
    recipient = [config("GMAIL_ACCT")]                  # Recipients
    subject = "New Blog Message!"                       # Set a subject line
    body = (f"Name: { name }\nEmail: { email }"
            + f"\nMessage: { message }")                           # Set body variable
    
    try:    # Attempt to connect to email server
        
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)    # Create a secure SSL connection
        connection.ehlo()   # Identify your email server to the host
        connection.login(user=send_from, password=password)     # Pass through your credentials
        
    except smtplib.SMTPAuthenticationError:     # If unable to authenticate
        
        print("Could not connect. Please check your authentication settings on your email server.")
        
        return False
        
    except TimeoutError:    # If connection timed out or server did not respond
        
        print("Unable to reach the host server. Please check your SSL and port settings.")
        
        return False
        
    else:   # Set up email content

        # Structure the body content
        email_string = f"Subject: {subject}\n\n{body}".format(subject, body)    # Structure the body content

        connection.sendmail(from_addr=send_from, to_addrs=recipient, msg=email_string)   # Pass data to server for email message
        
        print("Message has been sent.")
        
        connection.close()  # Close the connection
        
        return True