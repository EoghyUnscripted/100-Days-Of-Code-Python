"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 2
EXERCISE: 2-2 BMI Calculator
LEVEL: Beginner

INSTRUCTIONS:

    Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

    The BMI is a measure of some's weight taking into account their height.
    e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

    BMI = weight/height^2 = kg/meter^2

    Use the code provided -- do not change the existing code!

    CODE:

        height = input("enter your height in m: ")
        weight = input("enter your weight in kg: ")

        # WRITE YOUR CODE HERE

"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# BMI = weight/height^2 = kg/meter^2
bmi = float(weight) / float(height)**2
print(int(bmi))