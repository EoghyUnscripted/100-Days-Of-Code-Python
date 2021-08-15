"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 5
EXERCISE: 5-3 Adding Evens
LEVEL: Beginner

INSTRUCTIONS:

    You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
    Thus, the first even number would be 2 and the last one is 100:

        i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

    There should only be 1 print statement in your console output. 
    It should just print the final total and not every step of the calculation.

"""

sumEvens = 0

for n in range(2, 101, 2): 
    sumEvens += n

print(sumEvens)