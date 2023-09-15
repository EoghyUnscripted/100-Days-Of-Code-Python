"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 22
PROJECT: Pong Game
LEVEL: Intermediate

"""

from turtle import Screen, Turtle
from Modules import paddle, ball, scoreboard
import time

# Screen Setup
screen = Screen()   # Create new screen object
screen.setup(width=800, height=600)     # Set screen width and height
screen.bgcolor("black")     # Set screen background color
screen.title("Pong Game")  # Set title on screen
screen.tracer(0)    # Set tracer to 0

scores = scoreboard.Score() # Initialize scoreboard

r_paddle = paddle.Paddle((350, 0))  # Right Paddle Initializer
l_paddle = paddle.Paddle((-350, 0)) # Left Paddle Initializer

pong = ball.Ball()  # Ball Object Initializer

screen.listen() # Listens for key inputs

# Right Paddle Key Controls
screen.onkey(r_paddle.go_up, "Up")  # Moves right paddle object up when up arrow key is pressed
screen.onkey(r_paddle.go_down, "Down")  # Moves right paddle object down when down arrow key is pressed

# Left Paddle Key Controls
screen.onkey(l_paddle.go_up, "w")   # Moves left paddle object up when w key is pressed
screen.onkey(l_paddle.go_down, "s") # Moves left paddle object down when s key is pressed

# Screen Update Settings
game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed) # Set time interval between updates
    screen.update() # Update screen
    pong.move() # Constantly move ball object
    
    # Detect Wall Collision
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y() # Reverse ball object direction on the y axis
    
    # Detect Paddle Collision
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_x() # Reverse ball object direction on the x axis
        
    # Detect Right Player Paddle Misses
    if pong.xcor() > 380:
        pong.reset()    # Reset ball object position to center
        scores.l_point()    # Add point to other player
        
    # Detect Left Player Paddle Misses
    if pong.xcor() < -380:
        pong.reset()    # Reset ball object position to center
        scores.r_point()    # Add point to other player

screen.exitonclick()    # Sets listener for mouse click to close screen