"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 18
EXERCISE: 18-4 Turtle: Draw a Random Walk
LEVEL: Intermediate

"""

from turtle import Turtle, Screen
import random

# List of colors to pick from in program
colors = ["DeepPink", "DarkOrchid", "DarkGoldenrod", "CadetBlue", "DarkSlateGray",
          "DarkOrange", "DodgerBlue", "DeepSkyBlue4", "Magenta", "Moccasin"]

# List of directions to pick from in program
directions = [0, 90, 180, 270]

timmy = Turtle()    # Create turtle object
timmy.shape("turtle")   # Change shape
timmy.pensize(15)   # Change pen size
timmy.speed("fastest")      # Change speed


def change_direction():
    """Function used to change the direction of the turtle object at random."""
    random_direction = random.choice(directions)    # Get random direction heading
    timmy.setheading(random_direction)      # Set heading to new direction
    color = random.choice(colors)   # Get random color choice
    timmy.color(color)  # Change color
    timmy.forward(30)   # Move forward to draw line


for _ in range(300):    # Loops set count to draw lines
    change_direction()  # Call to change direction and draw line

screen = Screen()   # Opens screen
screen.exitonclick()    # Keeps screen open until clicked
