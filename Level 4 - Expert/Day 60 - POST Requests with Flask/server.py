"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 60
PROJECT: Blog Project - POST Form
LEVEL: Expert

"""


from datetime import datetime
import smtplib
import requests
from flask import Flask, render_template, request
from decouple import config
from Modules.post import Post

# Get filler blog posts
r = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
posts_list = []

# Loop through json data to create new post objects and add to list
for post in r:
    next_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_list.append(next_post)
    

app = Flask(__name__)
    

# Main route
@app.route("/")
def home():
    
    this_year = datetime.now().year
    
    return render_template("index.html", year=this_year, posts=posts_list)


# Blog route
@app.route("/post/<int:this_post>")
def get_post(this_post):
    
    this_year = datetime.now().year
    
    get_post = None
    
    # Match the requested post id to post object in list, return
    for post in posts_list:
        if post.id == this_post:
            get_post = post
    
    return render_template("post.html", year=this_year, post=get_post)


# About route
@app.route("/about")
def about():
    
    this_year = datetime.now().year
    
    return render_template("about.html", year=this_year)


# Contact route
@app.route("/contact", methods=['POST', 'GET'])
def contact():
    
    this_year = datetime.now().year
    c_get = "Contact Me"
    c_post = "Successfully sent your message!"
    
    if request.method == 'POST':
        
        data = request.form

        # for i in data:
        #     print(f"{str(i).capitalize()}: {data[i]}")
            
        send_email(data['name'], data['email'], data['phone'], data['message'])
        
        return render_template("contact.html", year=this_year, heading=c_post)
    
    elif request.method == 'GET':
    
        return render_template("contact.html", year=this_year, heading=c_get)


def send_email(name, email, phone, message):
    """ Function used to send email when contact form is filled out and posted. """
    
    print(name, email, phone, message)
    
    # NOTE: For security, I have not included my credentials. You will want to fill in your own depending on your service.
    
    # Set variables
    send_from = config("GMAIL_ACCT")                    # Email address
    password = config("GMAIL_PASSWORD")                 # Email password
    recipient = [config("GMAIL_ACCT")]                  # Recipients
    subject = "New Blog Message!"                       # Set a subject line
    body = (f"Name: { name }\nEmail: { email }"
            + f"\nPhone: { phone }\nMessage: "
            + f"{ message }")                           # Set body variable
    
    try:    # Attempt to connect to email server
        
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)    # Create a secure SSL connection
        connection.ehlo()   # Identify your email server to the host
        connection.login(user=send_from, password=password)     # Pass through your credentials
        
    except smtplib.SMTPAuthenticationError:     # If unable to authenticate
        
        print("Could not connect. Please check your authentication settings on your email server.")
        
    except TimeoutError:    # If connection timed out or server did not respond
        
        print("Unable to reach the host server. Please check your SSL and port settings.")
        
    else:   # Set up email content

        # Structure the body content
        email_string = f"Subject: {subject}\n\n{body}".format(subject, body)    # Structure the body content

        connection.sendmail(from_addr=send_from, to_addrs=recipient, msg=email_string)   # Pass data to server for email message
        
    finally:    # Always execute for security
        
        connection.close()  # Close the connection


if __name__ == "__main__":
    app.run(debug=True)