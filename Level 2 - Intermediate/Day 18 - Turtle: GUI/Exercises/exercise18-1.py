"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 18
EXERCISE: 18-1 Turtle: Draw a Square
LEVEL: Intermediate

"""

from turtle import Turtle, Screen

timmy = Turtle()    # Create Turtle object
timmy.shape("turtle")   # Change object shape
timmy.color("grey")     # Change object color
timmy.pencolor("purple")    # Change pen or line color
timmy.pensize(20)   # Change pen or line size

for _ in range(4):  # Loop 4 times
    timmy.forward(100)  # Move turtle object forward
    timmy.left(90)  # Turn object left

screen = Screen()   # Opens screen
screen.exitonclick()    # Keeps screen open until clicked
