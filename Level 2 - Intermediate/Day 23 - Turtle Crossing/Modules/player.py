"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 23
PROJECT: Turtle Crossing
LEVEL: Intermediate

"""

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()  # Extends Turtle class
        self.shape("turtle")    # Set object shape
        self.setheading(90)   # Point player object north
        self.penup()    # Pen up to prevent drawing on screen
        self.goto(0, -280) # Set position to move object when initiated
        self.finish_line = 280  # Set the y-cor for finish line

    def move(self):
        """ Function to move turtle on the y-axis. """
        new_y = self.ycor() + 10    # Get new y coordinate
        self.goto(self.xcor(), new_y)   # Go to new x, y coordinates on screen
        
    def reset(self):
        """ Function to reset turtle to starting position. """
        self.goto(0, -280)