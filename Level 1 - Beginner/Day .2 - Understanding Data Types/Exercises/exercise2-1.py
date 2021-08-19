"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 2
EXERCISE: 2-1 Data Types
LEVEL: Beginner

"""

two_digit_number = input("Type a two digit number: ")

# Checks that the unput is 2 digits
if len(two_digit_number) > 2:
  print("That is not a two digit number.\nTry, again.")
  exit

# If Valid Input
if len(two_digit_number) == 2:
  
  i = 0
  num = 0

  while i < 2:

    # Adds each number together
    num = num + int(two_digit_number[i])
    i += 1
      
  print(num)