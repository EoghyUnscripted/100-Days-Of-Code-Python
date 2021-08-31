"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 18
EXERCISE: 18-3 Turtle: Draw Different Shapes
LEVEL: Intermediate

"""

from turtle import Turtle, Screen
import random

# List of colors to pick from in program
colors = ["DeepPink", "DarkOrchid", "DarkGoldenrod", "CadetBlue", "DarkSlateGray",
          "DarkOrange", "DodgerBlue", "DeepSkyBlue4", "Magenta", "Moccasin"]

timmy = Turtle()    # Create turtle object
timmy.shape("turtle")   # Change shape
timmy.hideturtle()  # Hide object from view
timmy.penup()   # Pen up to avoid drawing lines
timmy.goto(-50, -200)   # Move object
timmy.showturtle()  # Show object in view
timmy.pendown()     # Pen down to draw lines


def draw_shape(sides):
    """Function to determine the shape to draw."""
    angle = 360 / sides     # Get the angle to rotate object

    for _ in range(sides):  # For number of sides
        timmy.forward(100)  # Move forward
        timmy.left(angle)   # Rotate to specified angle


for i in range(3, 11):  # Loops through shapes with 3 - 10 sides
    timmy.color(random.choice(colors))  # Choose a random color
    draw_shape(i)   # Call draw shape function with number of sides to draw

screen = Screen()   # Opens screen
screen.exitonclick()    # Keeps screen open until clicked
