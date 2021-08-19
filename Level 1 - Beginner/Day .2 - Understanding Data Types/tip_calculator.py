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

print("Welcome to the Tip Calculator.") # Print welcome greeting
bill = float(input("What is the total bill? $"))    # Get bill total
percent = float(input("What percent do you want to tip: Enter 10, 12 or 15?   % \x1B[4D"))  # Get percentage for tip

percent = percent / 100 # Convert to float
tipAmount = float(bill * percent)   # Get tip amount
billAmount = "{:.2f}".format(round(bill + tipAmount, 2))    # Calculate new bill amount with tip
message = f"The total bill with tip is: ${billAmount}"  # Output message with the bill amount with tip

print(message)

group = int(input("How many are splitting the bill, today? "))  # Get group count
split = "{:.2f}".format(round(float(billAmount) / group, 2))    # Calculate the split amount by person
message = f"Each person should pay: ${split}"   # Output message with split amount

print(message)
