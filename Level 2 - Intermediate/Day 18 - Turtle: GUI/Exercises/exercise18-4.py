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

colors = ["DeepPink", "DarkOrchid", "DarkGoldenrod", "CadetBlue", "DarkSlateGray",
          "DarkOrange", "DodgerBlue", "DeepSkyBlue4", "Magenta", "Moccasin"]

directions = [0, 90, 180, 270]

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")


def change_direction():
    random_direction = random.choice(directions)
    timmy.setheading(random_direction)
    color = random.choice(colors)
    timmy.color(color)
    timmy.forward(30)


for i in range(300):
    change_direction()

screen = Screen()
screen.exitonclick()
