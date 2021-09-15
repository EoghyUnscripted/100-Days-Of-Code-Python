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
