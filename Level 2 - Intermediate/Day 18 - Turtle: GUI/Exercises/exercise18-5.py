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

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_circle(offset):
    for _ in range(int(360/offset)):
        new_heading = (timmy.heading() + offset)
        timmy.setheading(new_heading)
        timmy.color(random_color())
        timmy.circle(100)
        print(_)


draw_circle(10)

screen = t.Screen()
screen.exitonclick()
