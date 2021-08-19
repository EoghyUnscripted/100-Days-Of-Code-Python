"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 5
PROJECT: PASSWORD GENERATOR
LEVEL: BEGINNER

"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for l in range(0, nr_letters):  # Loop through user input count
    # Get random letters from letters list and append each to password list
    password.append(random.choice(letters))

for s in range(0, nr_symbols):  # Loop through user input count
    # Get random symbols from symbols list and append each to password list
    password.append(random.choice(symbols))

for n in range(0, nr_numbers):  # Loop through user input count
    # Get random numbers from numbers list and append each to password list
    password.append(random.choice(numbers))

random.shuffle(password)    # Shuffle elements in password list
newPassword = ''.join(str(e) for e in password) # Join each element in the password list to string

print(f"Your password is: {newPassword}")