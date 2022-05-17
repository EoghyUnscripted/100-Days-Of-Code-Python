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

from turtle import Turtle
import pandas

class Score(Turtle):

    def __init__(self):
        super().__init__()  # Extends Turtle class
        self.penup()    # Pen up to prevent drawing
        self.hideturtle()   # Hide the object from view
        self.color("black")  # Set object color
        self.score = 0  # Set initial score
        self.correct_guesses = []   # Set list to store correct guesses
        self.output_list = []   # Set blank list to store names of states to learn


    def update_map(self, state, x, y):
        """ Function used to write correct guesses to the map. """
        self.goto(x,y)  # Move to coordinates on screen
        self.write(state, font=("Courier", 12, "normal"))   # Label the state on map
        self.correct_guesses.append(state)  # Append to correct guesses list
        
    def states_to_learn(self, states):
        """ Function used to write the missed states to a csv file on exit command. """
        for s in states:
            if s not in self.correct_guesses:
                self.output_list.append(s)
                
        data_dict = {
            "state": self.output_list
        }
        
        df = pandas.DataFrame(data_dict) # Pass list to dataframe
        df.to_csv("Level 2 - Intermediate/Day 25 - CSV Data, Pandas Library/Output/states_to_learn.csv") # Output to csv file