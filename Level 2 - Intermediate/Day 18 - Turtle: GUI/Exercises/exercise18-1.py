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

timmy = Turtle()
timmy.shape("turtle")
timmy.color("grey")
timmy.pencolor("purple")
timmy.pensize(20)

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()
