"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 38
PROJECT: Exercise Tracker
LEVEL: Advanced

"""

from Modules import api_caller

def get_Input():
    """ Function used to get user input for exercises they have completed. """

    user_input = input("What did you do for exercises, today?: ")       # Get user input
    
    results = api_caller.post_To_Nutritionix(user_input)        # Call Nutritionix API
    
    api_caller.post_To_Sheety(results)      # Call Sheety API
            
get_Input()     # Initial function call