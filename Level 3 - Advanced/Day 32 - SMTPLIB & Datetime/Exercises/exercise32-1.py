"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 32
EXERCISE: 32-1 Motivational Monday Quotes
LEVEL: Intermediate

"""

import smtplib
from random import randint
import json
import datetime as dt
import calendar

# NOTE: For security, I have not included my credentials. You will want to fill in your own depending on your service.

# Variables

send_from = "your@email.com"     # Email address
password = "yourPasswordHere"   # Email password
to = ['someone@email.com']   # Create a list of email recipients
subject = "Motivational Monday"    # Set a subject line

def send_motivation():
    """ Function used to send a new email with a motivational message. """
    
    # NOTE: This setup is using Gmail SMTP. You will want to use the SMTP based on your own email host.
    #       If using Gmail, check your security settings and set up an App Password for enhanced security.

    # SMTP Connection Setup

    try:    # Attempt to connect to email server
        
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)    # Create a secure SSL connection
        connection.ehlo()   # Identify your email server to the host
        connection.login(user=send_from, password=password)     # Pass through your credentials
        
    except smtplib.SMTPAuthenticationError:     # If unable to authenticate
        
        print("Could not connect. Please check your authentication settings on your email server.")
        
    except TimeoutError:    # If connection timed out or server did not respond
        
        print("Unable to reach the host server. Please check your SSL and port settings.")
        
    else:   # Set up email content
        
        with open("Level 3 - Advanced/Day 32 - SMTPLIB & Datetime/Exercises/Input/quotes.json") as data:
                
                quotes = json.load(data)    # Convert JSON to python dictionary
                new_quote = quotes[str(randint(1,25))]  # Pull a random quote
                body = f"{new_quote['quote']} \n {new_quote['author']}"     # Format body with quote details

        # Structure the body content
        message = f"Subject: {subject}\n\n{body}".format(subject, body)    # Structure the body content

        connection.sendmail(from_addr=send_from, to_addrs=to, msg=message)   # Pass data to server for email message
        
    finally:    # Always execute for security
        
        connection.close()  # Close the connection
        
def check_day():
    """ Function used to check the current day of the week. """
    
    now = dt.datetime.now()     # Get current date and time
    
    if now.weekday() == 0:  # If weekday returns 0 as Monday
        
        send_motivation()   # Call function to create and send email
        print("Motivation on the way...")   # Print message to console
        
    else:   # If weekday is not Monday
        
        print(f"Today is {calendar.day_name[now.weekday()]}. We didn't send an email.")     # Print message to console
        
check_day()     # Call function to check weekday