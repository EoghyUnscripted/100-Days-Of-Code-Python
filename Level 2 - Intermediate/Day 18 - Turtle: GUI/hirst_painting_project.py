"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 18
PROJECT: Hirst Painting
LEVEL: Intermediate

"""

import turtle as t
import random

timmy = t.Turtle()  # Create turtle object
t.colormode(255)    # Set colormode to accept RGB
timmy.speed("fastest")  # Set speed

# List of colors to pick from in program
color_list = [
    (245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245),
    (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19),
    (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50),
    (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20),
    (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)
]


def start_position():
    """Function used to set initial turtle object position on screen."""
    timmy.penup()   # Pen up to prevent drawing
    timmy.hideturtle()  # Hide turtle object from view
    timmy.setheading(225)   # Rotate to heading in degrees
    timmy.forward(330)  # Move forward
    timmy.showturtle()  # Shows turtle object in view
    timmy.setheading(0)     # Sets heading to 0


def next_row():
    """Function used to reset turtle object position on screen to beginning of row above last."""
    timmy.hideturtle()  # Hide turtle object from view
    timmy.setheading(90)    # Rotate left
    timmy.forward(50)   # Move forward
    timmy.setheading(180)   # Rotate left
    timmy.forward(500)  # Move to beginning of row
    timmy.showturtle()  # Shows turtle in view
    timmy.setheading(0)     # Sets heading to 0


def random_color():
    """Function used to choose random color from color list."""
    return random.choice(color_list)    # Returns RGB tuple


def draw_dots(rows, columns):
    """Function used to draw dots on screen."""
    start_position()    # Move turtle to starting position

    for _ in range(rows):   # For amount of rows
        for _ in range(columns):    # For amount of columns
            timmy.pendown()     # Pen down to draw
            timmy.dot(20, random_color())   # Draw dot
            timmy.penup()   # Pen up to prevent drawing line
            timmy.forward(50)   # Move forward
        next_row()  # Move turtle object to next row starting position

    timmy.hideturtle()  # Hide turtle object at end


draw_dots(10, 10)   # Calls function to draw dots with row and column count as parameters

screen = t.Screen()   # Opens screen
screen.exitonclick()    # Keeps screen open until clicked
