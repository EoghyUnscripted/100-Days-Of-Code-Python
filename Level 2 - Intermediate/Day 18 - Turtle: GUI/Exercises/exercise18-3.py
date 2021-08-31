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

colors = ["DeepPink", "DarkOrchid", "DarkGoldenrod", "CadetBlue", "DarkSlateGray",
          "DarkOrange", "DodgerBlue", "DeepSkyBlue4", "Magenta", "Moccasin"]

timmy = Turtle()
timmy.shape("turtle")
timmy.hideturtle()
timmy.penup()
timmy.goto(-50, -200)
timmy.showturtle()
timmy.pendown()


def draw_shape(sides):
    angle = 360 / sides

    for _ in range(sides):
        timmy.forward(100)
        timmy.left(angle)


for i in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(i)

screen = Screen()
screen.exitonclick()
