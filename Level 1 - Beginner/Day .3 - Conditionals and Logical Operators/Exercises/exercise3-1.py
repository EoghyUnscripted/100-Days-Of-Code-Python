"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 3
EXERCISE: 3-1 Odd or Even

INSTRUCTIONS:

    Write a program that works out whether if a given number is an odd or even number.

    Use the code provided -- do not change the existing code!

    CODE:

        number = int(input("Which number do you want to check? "))

        # WRITE YOUR CODE HERE

"""

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print(f"{number} is an even number.")
elif number % 2 != 0:
  print(f"{number} is an odd number.")