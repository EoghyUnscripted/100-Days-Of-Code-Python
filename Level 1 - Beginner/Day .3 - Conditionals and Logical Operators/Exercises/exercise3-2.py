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

"""

height = input("enter your height in m: ")  # Get user height
weight = input("enter your weight in kg: ") # Get user weight

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