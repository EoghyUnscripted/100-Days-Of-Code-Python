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

"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# BMI = weight/height^2 = kg/meter^2
bmi = float(weight) / float(height)**2
print(int(bmi))