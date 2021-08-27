"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 12
PROJECT: Guess the Number
LEVEL: Beginner

"""

from Modules import art
import random
import os

def clear():
    """Function used to clear the console."""
    os.system('clear') #on Linux System

print(art.logo) # Print logo
print("\nWelcome to Guess the Number!") # Print welcome message

level_choice = input("\nWhat level would you like to play? Easy or Hard? ") # Get level from user
number = random.choice(range(100))  # Get random number

lives = 0   # Set empty lives variable

# Set level
if level_choice == "easy":
    lives = 10  # Set lives to 10
elif level_choice == "hard":
    lives = 5   # Set lives to 5
else:   # If user enters anything else
    lives = 10  # Set lives to 10

while lives > 0: # While user has lives

    guess = input("\nMake a guess between 1 - 100: ")  # Get guess from user

    try:    # Check if guess converts to int
        int(guess)  # Try to coonvert to int
        is_int = True   # If converts, set true
        guess = int(guess)  # Convert guess to int
    except ValueError:  # If doesn't convert
        is_int = False  # Set false

    clear() # Clear the console

    print(art.logo) # Print logo

    if not is_int:  # If not an integer
        lives -= 1  # Remove a life
        print("\nYour guess must be a whole number between 1 - 100. Try again.") # Not a valid entry message
        print(f"You have ({lives}) remaining to guess the number.") # Print updated lives count
    elif guess == number: # If match
        lives = 0   # Set lives to 0 to stop game
        print(f"\nYou got it! The answer was {number}.\n")    # Print win message
    elif guess > number:    # If guess too high
        lives -= 1  # Remove a life
        print(f"\n{guess} is too high. Try again.") # Tell user guess was too high
        print(f"You have ({lives}) remaining to guess the number.") # Print updated lives count
    elif guess < number:    # If guess too low
        lives -= 1  # Remove a life
        print(f"\n{guess} is too low. Try again.")  # Tell user guess was too low
        print(f"You have ({lives}) remaining to guess the number.") # Print updated lives count