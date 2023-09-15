"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 22
PROJECT: Pong Game
LEVEL: Intermediate

"""

from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()  # Extends Turtle class
        self.penup()    # Pen up to prevent drawing
        self.hideturtle()   # Hide the object from view
        self.color("white")  # Set object color
        self.l_score = 0    # Set initial left player score
        self.r_score = 0    # Set initial right player score
        self.update_scores() # Get initial scores

    def update_scores(self):
        """ Function used to update scores displayed on screen. """
        self.clear()    # Clear the existing scores to re-write
        self.goto(-100, 200)    # Move position to left player score
        self.write(self.l_score, align="left", font=("Courier", 80, "normal"))  # Write left player score
        self.goto(100, 200) # Move position to right player score
        self.write(self.r_score, align="right", font=("Courier", 80, "normal")) # Write right player score
        
    def l_point(self):
        """ Function used to update left player score when right player misses ball. """
        self.l_score += 1   # Increment score by 1
        self.update_scores()    # Update scores on screen
        
    def r_point(self):
        """ Function used to update right player score when left player misses ball. """
        self.r_score += 1   # Increment score by 1
        self.update_scores()    # Update scores on screen