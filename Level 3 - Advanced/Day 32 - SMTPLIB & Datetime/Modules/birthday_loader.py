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

import pandas
from datetime import datetime as dt
from random import choice

def letter_generator(person):
    """ Function used to draft the body content of the email using an external text file. """
    
    # List of letter choices
    files = [
        "Level 3 - Advanced/Day 32 - SMTPLIB & Datetime/Input/letter_1.txt",
        "Level 3 - Advanced/Day 32 - SMTPLIB & Datetime/Input/letter_2.txt",
        "Level 3 - Advanced/Day 32 - SMTPLIB & Datetime/Input/letter_3.txt"
    ]
    
    file_name = choice(files)   # Get a random file path for new birthday email
    
    # Open file using name parameter
    with open(f"{file_name}") as body:
        message = body.read()   # Read the content of the file
        email_body = message.replace("[NAME]", f"{person}")     # Replace name placeholder with recipient name
    
    return email_body

def check_birthdays(birthdays):
    """ Function used to check the current day of the week and check for matching birthdays in external csv file. """
    
    today = (dt.now().month, dt.now().day)  # Creat a tuple with month and day
    
    if today in birthdays:  # If month, day is a key in birthdays dictionary
        
        return birthdays[today]
    
    else:   # If there is no match
        
        return False

def load_file():
    """ Function used to load birthday content from csv file. """
    
    # Get data from the provided csv file
    data = pandas.read_csv("Level 3 - Advanced/Day 32 - SMTPLIB & Datetime/Modules/birthdays.csv")

    # Convert to dictionary
    birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

    return check_birthdays(birthday_dict)