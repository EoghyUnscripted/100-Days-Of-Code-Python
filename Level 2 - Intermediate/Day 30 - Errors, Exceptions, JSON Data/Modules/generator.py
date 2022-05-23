"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 30
PROJECT: Password Manager
LEVEL: Intermediate

"""

from random import choice, randint, shuffle

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+'
    ]

def generate_password():
    """ Function used to generate and return a random password for user. """

    # Pass count, get random letters, symbols and number choices, append to password list
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)   # Shuffle the list

    # Convert to string
    password = "".join(password_list)
        
    return password