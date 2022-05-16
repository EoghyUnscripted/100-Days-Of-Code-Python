"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 24
EXERCISE: 24-1 Store Highest Score In a File
LEVEL: Intermediate

"""

from turtle import Turtle

alignment = "center"
font = ("Arial", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0     # Set initial points to 0
        self.high_score = self.file_high_score("r") # Set high score
        self.penup()    # Pen up to prevent drawing
        self.goto(0, 270)  # Go to new coordinates
        self.pendown()  # Pen down to draw
        self.color("grey")  # Set object color
        self.hideturtle()   # Hide the object from view
        self.update_score()     # Call function to write the score

    def update_score(self):
        """Function used to write the current score to the screen."""
        self.clear()    # Clear previous score from screen
        self.write(f"Score: {self.points} High Score: {self.high_score}", align=alignment, font=font)     # Writes the Score on screen
        
    def file_high_score(self, mode):
        """ Function to get or write new high score using a file based on parameter. """
        
        with open("Level 2 - Intermediate/Day 24 - Files, Directories, and Paths/Exercises/Modules/high_score.txt", mode=mode) as data:
            
            if mode == "r":
                contents = data.read()  # Read contents of file to return high score as intenger
                return int(contents)
            
            if mode == "w":
                data.write(f"{self.high_score}")    # Write new high score value to file

    def add_point(self):
        """Function used to update the score."""
        self.points += 1    # Add point to score
        self.update_score()     # Update score on screen

    def reset(self):
        """ Function used to reset the scoreboard and update new highest score if applicable. """
        if self.points > self.high_score:   # Check if ending score is a new high score
            self.high_score = self.points   # Replace old high score with new high score
            self.file_high_score("w")   # Call function to write new high scrore to file
        self.points = 0  # Reset gameplay score to 0
        self.update_score() # Write updated scores on refresh