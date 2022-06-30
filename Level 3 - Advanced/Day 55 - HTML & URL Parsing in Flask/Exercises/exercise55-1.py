"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 55
EXERCISE: 55-1 Logging Decorator Function
LEVEL: Advanced

"""

import random


# Set arg variables to pass
list_of_letters = ["A", "B", "C", "D", "E", "F"]
list_of_numbers = [num for num in range(len(list_of_letters))]
dict_of_pairs = [
    {0: {"A": 0}},
    {1: {"B": 1}},
    {2: {"C": 2}},
    {3: {"D": 3}},
    {4: {"E": 4}},
    {5: {"F": 5}}
]

# Create the logging_decorator
def logging_decorator(function):
    """ Function used to log data that passes through the decorator function. """
    
    def wrapper(*args):
        """ Inner function to perform. """
        
        # Log the name of the function called
        print(f"\nThe function called is: {function.__name__}\n")
        
        # Log the arguments given        
        print(f"\nThe arguments passed are:\n")
        
        arguments = [a for a in args]       # Create new list of arguments
        
        # Loop the arguments list
        for a in arguments:

            print(a)                        # Print the arguments in separate lines
        
        # Log the returned output of the function
        print(f"\nThe output is:\n{function(*args)}\n")
        
    return wrapper

# Use the logging_decorator
@logging_decorator
def some_function(count, letters, numbers, pairs):
    """ Function to get random elements from passed *args. """
    
    ran_num = random.randint(0, count - 1)      # Set range to select random int from
    letter = letters[ran_num]                   # Get the index using random int
    number = numbers[ran_num]                   # Get the index using random int
    pair = pairs[ran_num][ran_num]              # Get the corresponding dict pair
    
    # Output string
    out_string = (f"This Letter: {letter}\nThis Number: {number}\n"
                + f"Should Match: {pair}")
    
    return out_string

# Call the function
some_function(len(list_of_letters), list_of_letters, list_of_numbers, dict_of_pairs)