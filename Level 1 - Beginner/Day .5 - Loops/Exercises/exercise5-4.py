"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 5
EXERCISE: 5-4 FizzBuzz
LEVEL: Beginner

"""

for n in range(1, 101):
    if n % 5 == 0 and n % 3 == 0: # Divides by 5 and 3
        print("FizzBuzz")
    elif n % 5 == 0: # Divides only by 5
        print("Buzz")
    elif n % 3 == 0: # Divides only by 3
        print("Fizz")
    else: # Every other number
        print(n)