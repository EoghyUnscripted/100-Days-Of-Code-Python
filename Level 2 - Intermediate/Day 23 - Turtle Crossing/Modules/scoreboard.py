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

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()  # Extends Turtle class
        self.penup()    # Pen up to prevent drawing
        self.hideturtle()   # Hide the object from view
        self.color("black")  # Set object color
        self.level_num = 1  # Set starting level num
        self.update_score() # Get initial score
        
    def update_score(self):
        """ Function used to update current level on screen. """
        current_level = "Level: " + str(self.level_num)
        self.clear()    # Clear the existing score to re-write
        self.goto(-250, 250)    # Move position
        self.write(current_level, font=("Courier", 24, "normal"))  # Write level
        
    def next_level(self):
        """ Function to increase level. """
        self.level_num += 1
        self.update_score()
        
    def game_over(self):
        """ Function to display game over on screen. """
        self.goto(0, 0) # Move position
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))  # Write GAME OVER
        
