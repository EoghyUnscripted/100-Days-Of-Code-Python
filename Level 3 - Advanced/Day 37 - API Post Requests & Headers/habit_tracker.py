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

from decouple import config
from Modules import api_caller


# Variables

endpoint = config("PIXELA_GRAPH_ENDPOINT")      # Set endpoint url
api_key = config("PIXELA_API_KEY")              # Set API key
graph = config("PIXELA_GRAPH_ID")               # Set Pixela graph ID


def get_Input():
    """ Function used to get user input to update Pixela graph. """

    int_input = False       # Set boolean for input loop

    while not int_input:    # Loop until input is an integer
        
        try:    # Attempt to get integer input
            
            steps = int(input("How many steps did you walk, today?: "))      # Get input as int
        
        except ValueError:      # If other data type
            
            print("Sorry, you need to enter an integer.")       # Alert user they need to enter numbers only
            get_Input()                                         # Recursive call to repeat input call
            
        else:       # If input is integer
            
            api_caller.post_Pixel(endpoint, api_key, graph, str(steps))      # Call API to post steps to the tracker
            int_input = True        # Set True to end loop
            
get_Input()     # Initial function call