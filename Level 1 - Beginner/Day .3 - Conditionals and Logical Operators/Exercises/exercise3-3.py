"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 3
EXERCISE: 3-3 Leap Year
LEVEL: Beginner

"""

year = int(input("Which year do you want to check? "))  # Get user input year

# Checks if year divides by 4
if year % 4 == 0:
    # Checks if year also divides by 100
    if year % 100 == 0:
        # Checks if year also divides by 400
        if year % 400 == 0:
            print("Leap year.")
        # If does not also divide by 400
        else:
            print("Not leap year.")
    # If does not also divide by 100
    else:
        print("Leap year.")
        