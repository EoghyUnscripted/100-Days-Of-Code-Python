"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 2
PROJECT: TIP CALCULATOR
LEVEL: BEGINNER

"""

print("Welcome to the Tip Calculator.")
bill = float(input("What is the total bill? $"))
percent = float(input("What percent do you want to tip: Enter 10, 12 or 15?   % \x1B[4D"))

percent = percent / 100
tipAmount = float(bill * percent)
billAmount = "{:.2f}".format(round(bill + tipAmount, 2))
message = f"The total bill with tip is: ${billAmount}"

print(message)

group = int(input("How many are splitting the bill, today? "))
tip = "{:.2f}".format(round(float(billAmount) / group, 2))
message = f"Each person should pay: ${tip}"

print(message)
