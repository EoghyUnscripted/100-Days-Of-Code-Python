"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 24
EXERCISE: 24-1 Store Highest Score In a File
LEVEL: Intermediate

"""

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")    # Set shape of object to circle
        self.penup()    # Pen up to prevent drawing
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # Set object size on screen
        self.color("blue")  # Set object color
        self.speed("fastest")   # Set speed of object
        self.refresh()  # Call refresh function

    def refresh(self):
        """Function used to refresh object position on screen."""
        ran_x = random.randint(-280, 280)   # Get random x integer
        ran_y = random.randint(-280, 280)   # Get random y integer
        self.goto(ran_x, ran_y)     # Go to the new random coordinates
