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

timmy = Turtle()
timmy.shape("turtle")
timmy.color("grey")
timmy.pencolor("purple")

for _ in range(4):
    for _ in range(10):
        timmy.pd()
        timmy.forward(10)
        timmy.pu()
        timmy.forward(10)
    timmy.left(90)

screen = Screen()
screen.exitonclick()
