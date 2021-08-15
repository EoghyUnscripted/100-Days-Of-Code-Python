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

INSTRUCTIONS:

    You are going to write a program that automatically prints the solution to the FizzBuzz game. 

    Your program should print each number from 1 to 100 in turn.
    When the number is divisible by 3 then instead of printing the number it should print "Fizz".
    When the number is divisible by 5, then instead of printing the number it should print "Buzz".
    And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

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