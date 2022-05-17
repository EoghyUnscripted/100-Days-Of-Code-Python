"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 25
PROJECT: U.S. States Game
LEVEL: Intermediate

"""

import turtle
import pandas
from Modules import scoreboard

# Get data from the provided csv file 
data = pandas.read_csv("Level 2 - Intermediate/Day 25 - CSV Data, Pandas Library/Modules/50_states.csv")

# Get the state names into a list
state_names = data['state'].to_list()

# Screen Setup
screen = turtle.Screen()    # Initialize screen object
screen.title("U.S. States Game")    # Set screen title
image = "Level 2 - Intermediate/Day 25 - CSV Data, Pandas Library/Images/blank_states_img.gif"  # Set image path
screen.addshape(image)  # Load image as new shape
turtle.shape(image) # Set image

score = scoreboard.Score()  # Initialize scoreboard object

# Loop game until user guesses all 50 states
while len(score.correct_guesses) < 50:
    
    # Prompt user for a guess
    answer_state = screen.textinput(title=f"{len(score.correct_guesses)}/50 Correct", prompt="Guess the name of a state:")
    
    # Check if user requests to exit game
    if answer_state == None or answer_state.title() == "Exit":
        score.states_to_learn(state_names)  # Call function to write missed guesses to file
        break   # Break loop, end game
        
    # Check if guess is correct
    if answer_state in state_names:
        row = data[data.state == answer_state]  # Validate state is in the list
        score.update_map(row.state.item(), int(row.x), int(row.y))  # Call function to update game
        