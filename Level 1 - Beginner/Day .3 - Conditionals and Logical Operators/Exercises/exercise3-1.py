"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 3
EXERCISE: 3-1 Odd or Even
LEVEL: Beginner

"""

number = int(input("Which number do you want to check? "))  # Get user input

# Check if divides by 2
if number % 2 == 0:
  print(f"{number} is an even number.")
# If does not
elif number % 2 != 0:
  print(f"{number} is an odd number.")