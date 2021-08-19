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

"""

age = input("What is your current age? ")

days = (90 - int(age)) * 365    # Sets Days by subtracting 90 - input multiplied by 365
weeks = (90 - int(age)) * 52    # Sets Weeks by subtracting 90 - input multiplied by 52
months = (90 - int(age)) * 12   # Sets Months by subtracting 90 - input multiplied by 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")