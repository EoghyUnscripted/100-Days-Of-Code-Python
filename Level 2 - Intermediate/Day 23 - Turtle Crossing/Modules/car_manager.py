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
import random

class CarManager:
    
    def __init__(self):
        self.all_cars = []   # List to store new cars
        self.move_distance = 5  # Set initial move distance
        self.move_increments = 5 # Set increments to increase each level
        
    def create_cars(self):
        """ Function used to generate new cars for gameplay. """
        COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] # Color choices for random pick
        random_generation = random.randint(1, 6)    # Get a random integer

        # Generate a new car if random_generation is 1
        if random_generation == 1:
            new_car = Turtle("square")  # Set object shape
            new_car.shapesize(stretch_wid=1, stretch_len=2) # Set object dimensions
            new_car.penup() # Pen up to prevent drawing
            new_car.color(random.choice(COLORS))    # Get random color choice
            random_y = random.randint(-250, 250)    # Get random integer on y axis
            new_car.goto(300, random_y) # Move to position
            self.all_cars.append(new_car)   # Append to all cars list
        
    def move_cars(self):
        """ Function used to move all car objects across screen during gameplay. """
        for c in self.all_cars:
            c.backward(self.move_distance)  # Move each car object across the screen by set increments
            
    def increase_speed(self):
        """ Function used to increase speed of car objects each level up. """
        self.move_distance += self.move_increments  # Increase speed by set increments
