"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 19
EXERCISE: 19-1 Turtle: Etch-A-Sketch
LEVEL: Intermediate

"""

import turtle as t

timmy = t.Turtle()  # Create new turtle object


def forward():
    """Function used to move turtle object forward."""
    timmy.forward(10)   # Move forward 10 spaces


def backward():
    """Function used to move turtle object backward."""
    timmy.back(10)  # Move backward 10 spaces


def counter():
    """Function used to turn turtle object counter-clockwise."""
    timmy.left(10)  # Turn left by 10 degrees


def clockwise():
    """Function used to turn turtle object clockwise."""
    timmy.right(10)     # Turn right by 10 degrees


def clear_screen():
    """Function used to clear screen and move turtle to original position."""
    timmy.clear()   # Clear screen of drawing
    timmy.penup()   # Pen up to prevent drawing
    timmy.home()    # Move turtle object back to original position
    timmy.pendown()     # Pen down to start drawing


t.listen()      # Listens for key inputs
t.onkey(fun=forward, key="w")   # When 'w' is pressed, move forward
t.onkey(fun=backward, key="s")  # When 's' is pressed, move backward
t.onkey(fun=counter, key="a")   # When 'a' is pressed, turn counter-clockwise
t.onkey(fun=clockwise, key="d")     # When 'd' is pressed, turn clockwise
t.onkey(fun=clear_screen, key="c")  # When 'c' is pressed, clear screen, return to original position
t.exitonclick()    # Keeps screen open until clicked
