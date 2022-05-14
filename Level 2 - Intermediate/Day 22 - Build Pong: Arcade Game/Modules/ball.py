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

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()  # Extends Turtle class
        self.shape("circle")    # Set object shape
        self.color("white") # Set object color
        self.penup()    # Pen up to prevent drawing on screen
        self.x_move = 10    # Set variable for move increment on x axis
        self.y_move = 10    # Set variable for move increment on y axis
        self.move_speed = 0.1   # Set initial speed of ball object
        
    def move(self):
        """ Function that moves the ball object across the screen. """
        new_x = self.xcor() + self.x_move   # Get new x coordinate
        new_y = self.ycor() + self.y_move   # Get new y coordinate
        self.goto(new_x, new_y) # Move object to new x, y coordinates
        
    def bounce_y(self):
        """ Function used to reverse direction of ball object when it collides with the screen wall. """
        self.y_move *= -1   # Reverse movement direction on the y axis
        
    def bounce_x(self):
        """ Function used to reverse direction of ball object when it collides with a paddle. """
        self.x_move *= -1   # Reverse movement direction on the x axis
        self.move_speed *= 0.9  # Increase the move speed of the ball object

    def reset(self):
        """ Function used to reset ball object to (0, 0) and move in the opposite direction during play when a player misses the ball. """
        self.goto(0, 0) # Move object to center of screen
        self.move_speed = 0.1   # Reset the ball speed to initial
        self.bounce_x() # Reverse direction of the object on the x axis