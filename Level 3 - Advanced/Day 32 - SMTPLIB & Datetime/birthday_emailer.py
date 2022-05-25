"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 32
PROJECT: Automated Birthday Emailer
LEVEL: Advanced

"""

from Modules import birthday_loader as loader
from Modules import emailer

birthdays = loader.load_file()     # Get birthdays for today

if birthdays is False:  # If no birthdays match today
    
    print("There are no birthdays, today.")     # Print message to console

else:   # If there are birthdays today
    
    # NOTE: For security, I have not included my credentials. You will want to fill in your own depending on your service.
    
    # Set variables
    
    send_from = "your@email.com"     # Email address
    password = "yourPassword"   # Email password
    recipient = [birthdays['email']]   # Create a list of email recipients
    subject = "Happy Birthday!"    # Set a subject line
    body = loader.letter_generator(birthdays['name'])   # Set body variable
    
    emailer.send_Birthday_Wishes(send_from, password, recipient, subject, body)    # Call function to send email