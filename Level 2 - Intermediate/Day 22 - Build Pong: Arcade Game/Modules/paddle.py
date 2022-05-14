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

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()  # Extends Turtle class
        self.shape("square")    # Set object shape
        self.color("white") # Set object color
        self.shapesize(stretch_wid=5, stretch_len=1)    # Set shape dimensions
        self.penup()    # Pen up to prevent drawing on screen
        self.goto(position) # Set position to move object when initiated
        
    def go_up(self):
        """ Function to move paddle up on screen. """
        new_y = self.ycor() + 20    # Get new y coordinate
        self.goto(self.xcor(), new_y)   # Go to new x, y coordinates on screen
        
    def go_down(self):
        """ Function to move paddle down on screen. """
        new_y = self.ycor() - 20    # Get new y coordinate
        self.goto(self.xcor(), new_y)   # Go to new x, y coordinates on screen