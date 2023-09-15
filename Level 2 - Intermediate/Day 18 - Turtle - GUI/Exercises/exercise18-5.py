"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 18
EXERCISE: 18-5 Turtle: Draw a Spirograph
LEVEL: Intermediate

"""

import turtle as t
import random

timmy = t.Turtle()  # Create turtle object
t.colormode(255)    # Set colormode to accept RGB
timmy.speed("fastest")  # Set speed


def random_color():
    """Function to get and return a random color RGB value as tuple."""
    r = random.randint(0, 255)  # Set red
    g = random.randint(0, 255)  # Set green
    b = random.randint(0, 255)  # Set blue
    color = (r, g, b)   # Create tuple with values
    return color    # Return tuple


def draw_circle(offset):
    """Function used to draw circles with turtle object."""
    # Loop used to calculate how many circles to draw to complete
    for _ in range(int(360/offset)):    # If offset 10 spaces, loops 360/10 times
        new_heading = (timmy.heading() + offset)    # Get new heading
        timmy.setheading(new_heading)   # Set new heading
        timmy.color(random_color())     # Get random pen color
        timmy.circle(100)   # Draw circles


draw_circle(10)     # Call function with offset as parameter

screen = t.Screen()   # Opens screen
screen.exitonclick()    # Keeps screen open until clicked
