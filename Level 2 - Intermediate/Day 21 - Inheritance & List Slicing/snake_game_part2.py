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
screen = Screen()   # Create new screen object
screen.setup(width=600, height=600)     # Set screen width and height
screen.bgcolor("black")     # Set screen background color
screen.title("Snake Game")  # Set title on screen
screen.tracer(0)    # Set tracer to 0

sammy = snake.Snake()   # Create new snake object
food = food.Food()      # Create new food object
score = scoreboard.Score()      # Create new scoreboard object
screen.listen()     # Listens for key inputs


def game_play():
    """Function used to start game."""
    game_is_running = True  # Set boolean for while loop

    while game_is_running:  # While boolean is true
        screen.update()     # Update screen
        time.sleep(0.3)     # Set time interval between updates
        sammy.move()        # Constantly move snake forward

        # Detect collision with food object
        if sammy.head.distance(food) < 15:
            food.refresh()  # Refreshes the objects position on screen
            sammy.extend()  # Adds another segment to the snake tail
            score.add_point()   # Add point to the scoreboard

        # Detect collision with the walls
        if sammy.head.xcor() > 290 or sammy.head.xcor() < -290 or sammy.head.ycor() > 290 or sammy.head.ycor() < -290:
            game_is_running = False     # Set game play to False and ends
            score.game_over()   # Call to write GAME OVER on screen

        # Detect collision with tail
        for segment in sammy.turtle_list[1:]:
            if sammy.head.distance(segment) < 10:
                game_is_running = False  # Set game play to False and ends
                score.game_over()  # Call to write GAME OVER on screen


screen.onkey(sammy.left, "Left")   # When 'Left Arrow' is pressed, turn West
screen.onkey(sammy.right, "Right")     # When 'Right Arrow' is pressed, turn East
screen.onkey(sammy.up, "Up")   # When 'Up Arrow' is pressed, turn North
screen.onkey(sammy.down, "Down")     # When 'Down Arrow' is pressed, turn South
screen.onkey(game_play, "space")    # When 'Space' is pressed, start game

screen.exitonclick()    # Sets listener for mouse click to close screen

