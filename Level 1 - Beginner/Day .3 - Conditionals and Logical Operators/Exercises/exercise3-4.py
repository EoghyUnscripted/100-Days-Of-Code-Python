"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 3
EXERCISE: 3-4 Pizza Order
LEVEL: Beginner

"""

print("Welcome to Python Pizza Deliveries!")    # Prints welcome greeting
size = input("What size pizza do you want? S, M, or L ")    # Gets size choice from user
add_pepperoni = input("Do you want pepperoni? Y or N ") # Gets peperroni choice from user
extra_cheese = input("Do you want extra cheese? Y or N ")   # Gets extra cheese choice from user

# Convert inputs to uppercase
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

# Check that entries are valid
if size not in ['L','M','S']:   # Checks that size is S, M or L for input
    print('Please enter S, M, or L for size.')  # Outputs message if error
elif add_pepperoni not in ['N', 'Y']:   # Checks that input is Y or N
    print('Please use Y or N to make your selection for pepperoni.')    # Outputs message if error
elif extra_cheese not in ['N', 'Y']:    # Checks that input is Y or N
    print('Please use Y or N to make your selection for extra cheese.') # Outputs message if error

# Calculate order price
if size == 'L': # Calculate large pizza
    order = 25  # Sets base price
    if add_pepperoni == 'Y':   # Adds price for pepperoni
        order += 3  # Calculates added price
    if extra_cheese == 'Y':    # Adds price for extra cheese
        order += 1  # Calculates added price
elif size == 'M':   # Calculate medium pizza
    order = 20  # Sets base price
    if add_pepperoni == 'Y':   # Adds price for pepperoni
        order += 3  # Calculates added price
    if extra_cheese == 'Y':    # Adds price for extra cheese
        order += 1  # Calculates added price
elif size == 'S':   # Calculate small pizza
    order = 15  # Sets base price
    if add_pepperoni == 'Y':   # Adds price for pepperoni
        order += 2  # Calculates added price
    if extra_cheese == 'Y':    # Adds price for extra cheese
        order += 1  # Calculates added price

print(f'Your final bill is: ${order}.')  # Output total to user