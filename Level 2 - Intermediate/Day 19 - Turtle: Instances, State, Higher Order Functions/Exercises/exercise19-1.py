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

timmy = t.Turtle()


def forward():
    timmy.forward(10)


def backward():
    timmy.back(10)


def counter():
    timmy.left(10)


def clockwise():
    timmy.right(10)


def clear_screen():
    timmy.clear()


t.listen()
t.onkey(fun=forward, key="w")
t.onkey(fun=backward, key="s")
t.onkey(fun=counter, key="a")
t.onkey(fun=clockwise, key="d")
t.onkey(fun=clear_screen, key="c")
t.exitonclick()    # Keeps screen open until clicked
