"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 3
EXERCISE: 3-2 BMI Calculator 2.0
LEVEL: Beginner

INSTRUCTIONS:

    Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

    The BMI is a measure of some's weight taking into account their height.
    e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

    Calculate BMI with this formula:

        BMI = weight/height^2 = kg/meter^2

    It should tell them the interpretation of their BMI based on the BMI value:

        Under 18.5 they are underweight
        Over 18.5 but below 25 they have a normal weight
        Over 25 but below 30 they are slightly overweight
        Over 30 but below 35 they are obese
        Above 35 they are clinically obese.

    Your output should be formatted like the lines below:

        "Your BMI is 18, you are underweight."
        "Your BMI is 22, you have a normal weight."
        "Your BMI is 28, you are slightly overweight."
        "Your BMI is 33, you are obese."
        "Your BMI is 40, you are clinically obese."

    Use the code provided -- do not change the existing code!

    CODE:

        height = input("enter your height in m: ")
        weight = input("enter your weight in kg: ")

        # WRITE YOUR CODE HERE

"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# BMI = weight/height^2 = kg/meter^2
bmi = round(float(weight) / float(height)**2)

# Checks the output of BMI Calulation for response
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")