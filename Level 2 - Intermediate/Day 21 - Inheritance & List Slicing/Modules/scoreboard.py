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

from turtle import Turtle

alignment = "center"
font = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0     # Set initial points to 0
        self.penup()    # Pen up to prevent drawing
        self.goto(0, 270)  # Go to new coordinates
        self.pendown()  # Pen down to draw
        self.color("grey")  # Set object color
        self.hideturtle()   # Hide the object from view
        self.update_score()     # Call function to write the score

    def update_score(self):
        """Function used to write the current score to the screen."""
        self.write(f"Score: {self.points}", align=alignment, font=font)     # Writes the Score on screen

    def add_point(self):
        """Function used to update the score."""
        self.points += 1    # Add point to score
        self.clear()    # Clear previous score from screen
        self.update_score()     # Update score on screen

    def game_over(self):
        """Function used to write GAME OVER on the screen."""
        self.penup()    # Pen up to prevent drawing
        self.goto(0, 0)     # Move the object to the center of screen
        self.pendown()      # Pen down to draw
        self.write("GAME OVER", align=alignment, font=font)     # Write GAME OVER on screen
