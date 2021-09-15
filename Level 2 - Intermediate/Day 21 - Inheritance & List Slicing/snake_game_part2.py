"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 21
PROJECT: Snake Game Part 2
LEVEL: Intermediate

"""
import time
from turtle import Screen
from Modules import snake, food, scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

sammy = snake.Snake()
food = food.Food()
score = scoreboard.Score()
screen.listen()     # Listens for key inputs


def game_play():
    """Function used to start game."""

    game_is_running = True

    while game_is_running:
        screen.update()
        time.sleep(0.3)
        sammy.move()

        if sammy.head.distance(food) < 15:
            food.refresh()
            sammy.extend()
            score.add_point()

        if sammy.head.xcor() > 290 or sammy.head.xcor() < -290 or sammy.head.ycor() > 290 or sammy.head.ycor() < -290:
            game_is_running = False
            score.game_over()

        for segment in sammy.turtle_list[1:]:
            if sammy.head.distance(segment) < 10:
                game_is_running = False
                score.game_over()


screen.onkey(sammy.left, "Left")   # When 'Left Arrow' is pressed, turn West
screen.onkey(sammy.right, "Right")     # When 'Right Arrow' is pressed, turn East
screen.onkey(sammy.up, "Up")   # When 'Up Arrow' is pressed, turn North
screen.onkey(sammy.down, "Down")     # When 'Down Arrow' is pressed, turn South
screen.onkey(game_play, "space")    # When 'Space' is pressed, start game

screen.exitonclick()

