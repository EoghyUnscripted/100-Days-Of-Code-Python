"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 23
PROJECT: Turtle Crossing
LEVEL: Intermediate

"""

import time
from turtle import Screen
import turtle
from Modules import car_manager, player, scoreboard

# Screen Setup
screen = Screen()   # Create new screen object
screen.setup(width=600, height=600)     # Set screen width and height
screen.title("Turtle Crossing")  # Set title on screen
screen.tracer(0)    # Set tracer to 0

timmy = player.Player() # Initialize player object
cars = car_manager.CarManager() # Initialize car manager
scores = scoreboard.Scoreboard() # Initialize scoreboard

screen.listen() # Listens for key inputs

screen.onkey(timmy.move, "Up")  # Moves player object up when up arrow key is pressed

# Screen Update Settings
game_is_on = True
while game_is_on:
    time.sleep(0.1) # Set time interval between updates
    screen.update() # Update screen
    
    cars.create_cars()  # Generate new cars
    cars.move_cars()    # Move cars across screen
    
    # Detect collision with car
    for c in cars.all_cars:
        if c.distance(timmy) < 20:
            game_is_on = False  # Set gameplay to false and end
            scores.game_over()  # Write game over on screen
    
    # Detect successful crossing
    if timmy.ycor() > timmy.finish_line:
        timmy.reset()   # Reset to starting position for next level
        scores.next_level() # Set game to next level and update score
        cars.increase_speed()   # Increase speed of cars
    
    
screen.exitonclick()    # Sets listener for mouse click to close screen