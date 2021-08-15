"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 2
EXERCISE: 2-3 Your Life in Weeks, Months, Years
LEVEL: Beginner

INSTRUCTIONS:

    Create a program using maths and f-Strings that tells us how many days, weeks, 
    months we have left if we live until 90 years old.

    It will take your current age as the input and output a message with our time left in this format:
    You have x days, y weeks, and z months left.

    Use the code provided -- do not change the existing code!

    CODE:

        age = input("What is your current age? ")

        # WRITE YOUR CODE HERE

"""

age = input("What is your current age? ")

days = (90 - int(age)) * 365
weeks = (90 - int(age)) * 52
months = (90 - int(age)) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")