"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 4
EXERCISE: 4-2 Who's Paying?

INSTRUCTIONS:

    You are going to write a program which will select a random name from a list of names.
    The person selected will have to pay for everybody's food bill.

    You are not allowed to use the choice() function!

    Use the code provided -- do not change the existing code!

    CODE:

      names_string = input("Give me everybody's names, separated by a comma. ")
      names = names_string.split(", ")

"""

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

randomNum = random.randint(0,len(names)-1)

print(f"{names[randomNum]} is going to buy the meal today!")