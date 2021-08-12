"""
INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

"""

# DAY: 2
# EXERCISE: TIP CALCULATOR

# INSTRUCTIONS:
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the Tip Calculator.")
bill = float(input("What is the total bill?\n"))
percent = float(input("What percent do you want to tip: Enter 10, 12 or 15?\n"))

percent = percent / 100
tipAmount = float(bill * percent)
billAmount = round(bill + tipAmount, 2)
message = f"The total bill with tip is: ${billAmount}"

print(message)

group = int(input("How many are splitting the bill, today?\n"))
tip = round(billAmount / group, 2)
message = f"Each person should pay: ${tip}"

print(message)