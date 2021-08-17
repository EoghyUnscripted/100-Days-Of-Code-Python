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

INSTRUCTIONS:

    You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. 
    
    Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

        number of cans = (wall height ✖️ wall width) ÷ coverage per can. 
            e.g. Height = 2, Width = 4, Coverage = 5

        number of cans = (2 ✖️ 4) ÷ 5 = 1.6

    But because you can't buy 0.6 of a can of paint, the result should be rounded up. 

    NOTE: The name of the function and parameters must match those for paint_calc() for the code to work.

    Use the code provided -- do not change the existing code!

    CODE:

        # WRITE YOUR CODE HERE

        test_h = int(input("Height of wall: "))
        test_w = int(input("Width of wall: "))
        coverage = 5
        paint_calc(height=test_h, width=test_w, cover=coverage)

"""

import math

def paint_calc(height, width, cover):
    
    number_of_cans = int(math.ceil((height * width)/cover)) # Round up to nearest number
    print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input("Height of wall: ")) # Get Height of wall
test_w = int(input("Width of wall: "))  # Get Width of wall
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage) # Call function with parameters