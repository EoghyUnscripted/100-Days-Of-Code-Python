"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 13
EXERCISE: 13-1 Debugging Odd or Even
LEVEL: Beginner
"""

number = int(input("Which number do you want to check?"))

if number % 2 == 0: # Changed = to ==
  print("This is an even number.")
else:
  print("This is an odd number.")