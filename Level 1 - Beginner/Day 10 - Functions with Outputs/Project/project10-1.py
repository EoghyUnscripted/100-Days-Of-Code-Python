"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 10
PROJECT: 10-1 Calculator: Combining Dictionaries and Functions
LEVEL: Beginner

"""

def add(n1, n2):
    """Function that adds two numbers as parameters and returns the result."""
    return n1 + n2

def subtract(n1, n2):
    """Function that subtracts two numbers as parameters and returns the result."""
    return n1 - n2

def multiply(n1, n2):
    """Function that multiplies two numbers as parameters and returns the result."""
    return n1 * n2

def divide(n1, n2):
    """Function that divides two numbers as parameters and returns the result."""
    return n1 / n2

# Dictionary to store functions as operations
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

# Gets the keys from operations dictionary and prints in console
for o in operations:
    print(o)

num1 = int(input("What is the first number?: "))    # Get first number from user
num2 = int(input("What is the second number?: "))   # Get second number from user
operator_symbol = input("Pick an operation to perform: ")   # Get operation to use from user

# Checks if operation key is in the operation dictionary
if operator_symbol in operations:
    # Calls the function assigned to the operation key
    answer = operations[operator_symbol](num1, num2)

print(f"{num1} {operator_symbol} {num2} = {answer}")    # Output result