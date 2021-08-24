"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 10
PROJECT: 10-1 Calculator: While Loops, Flags, and Recursion
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

def calculator():
    """Function that gets numbers and operation from user to calculate and output a mathematial result."""
    
    # Dictionary to store functions as operations
    operations_dictionary = {
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide
    }

    def operators():
        """Function that gets the operation keys from dictionary and outputs as a comma separated string."""
        
        o_string = ""   # Set empty variable for use with join statement

        # Gets all operator keys from dictionary and sets a string
        for o in operations_dictionary:
            o_string += o

        options = ", ".join(o_string) # Joins the characters in string with commas
        return options  # Returns the formatted string

    num1 = int(input("What is the first number?: "))    # Get first number from user

    should_continue = True  # Sets boolean flag to loop program or to stop

    while should_continue:
        
        print(operators())  # Print operator keys string to user
        operator_symbol = input("Pick an operation to perform: ")   # Get operation from user
        num2 = int(input("What is the next number?: ")) # Get next number from user

        # If the operation key is in the dictionary
        if operator_symbol in operations_dictionary:
            calculation = operations_dictionary[operator_symbol]    # Set the key function name to variable
            answer = calculation(num1, num2)    # Calls function and sets return value to variable

        print(f"{num1} {operator_symbol} {num2} = {answer}")    # Prints output to user

        # Input message asking user what they want to do next
        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()

        if continue_calculation == "y": # If they want to continue calculating with previous result
            num1 = answer   # Sets first number as previous result
        elif continue_calculation == "n":   # If they want to continue calculating with new calculation
            should_continue = False # Sets loop condition to false and ends current run
            calculator()    # Recursive function call to restart program
        else:   # Any other input
            should_continue = False # Sets loop condition to false and ends program

calculator()    # Initial function call