"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 4
EXERCISE: 4-2 Who's Paying?
LEVEL: Beginner

"""

import random

names_string = input("Give me everybody's names, separated by a comma. ") # Get the list of names
names = names_string.split(", ")  # Format names with comma separators

randomNum = random.randint(0,len(names)-1)  # Get a random number for index selection

print(f"{names[randomNum]} is going to buy the meal today!")  # Pick random number and select person from list