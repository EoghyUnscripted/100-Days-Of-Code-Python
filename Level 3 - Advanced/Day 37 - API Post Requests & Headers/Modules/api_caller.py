"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 37
PROJECT: Habit Tracker
LEVEL: Advanced

"""

import requests
from datetime import datetime as dt


def post_Pixel(endpoint, key, graph, steps):
    """ Function used to post a Pixel to the habit tracker graph. """
    
    today = dt.strptime("20220530", "%Y%m%d")    # Create date object for today
    
    # Pixela API Parameters
    headers = {
        "X-USER-TOKEN": key     # Pass API Key
    }
    
    data = {
        "date": today.strftime('%Y%m%d'),    # Convert to yyyyMMdd format as string
        "quantity": "0"                      # Input as int for graph update
    }
    
    r = requests.post(f"{endpoint}/{graph}", json=data, headers=headers)    # Post to API
    print(r.text)       # Print response message
    

