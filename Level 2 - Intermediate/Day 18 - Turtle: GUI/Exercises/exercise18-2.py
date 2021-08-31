"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 18
EXERCISE: 18-2 Turtle: Draw a Dashed Line
LEVEL: Intermediate

"""

from turtle import Turtle, Screen

timmy = Turtle()    # Create Turtle object
timmy.shape("turtle")   # Change object shape
timmy.color("grey")     # Change object color
timmy.pencolor("purple")    # Change pen or line color

for _ in range(4):  # Loop 4 times for square
    for _ in range(10):     # Loops 10 times for dashes
        timmy.pd()  # Pen down to draw line
        timmy.forward(10)   # Move forward
        timmy.pu()  # Pen up for blank space
        timmy.forward(10)   # Move forward
    timmy.left(90)  # Turn left

screen = Screen()   # Opens screen
screen.exitonclick()    # Keeps screen open until clicked
