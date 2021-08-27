"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 13
EXERCISE: 13-2 Debugging FizzBuzz
LEVEL: Beginner
"""

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # Replaced or with and
    print("FizzBuzz")
  elif number % 3 == 0: # Changed from if to elif
    print("Fizz")
  elif number % 5 == 0: # Changed from if to elif
    print("Buzz")
  else:
    print(number) # Removed brackets