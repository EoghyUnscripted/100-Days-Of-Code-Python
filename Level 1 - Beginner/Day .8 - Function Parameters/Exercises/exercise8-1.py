"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 8
EXERCISE: 8-1 Paint Area Calculator
LEVEL: Beginner

"""

import math

def paint_calc(height, width, cover):
    
    number_of_cans = int(math.ceil((height * width)/cover)) # Round up to nearest number
    print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input("Height of wall: ")) # Get Height of wall
test_w = int(input("Width of wall: "))  # Get Width of wall
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage) # Call function with parameters