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

def check_guess(guess, lives, number):

    clear() # Clear the console
    print(art.logo) # Print logo

    try:    # Check if guess converts to int
        int(guess)  # Try to coonvert to int
        is_int = True   # If converts, set true
        guess = int(guess)  # Convert guess to int
    except ValueError:  # If doesn't convert
        is_int = False  # Set false

    if not is_int:  # If not an integer
        print("\nYour guess must be a whole number between 1 - 100. Try again.") # Not a valid entry message
        return lives - 1  # Remove a life
    elif guess == number: # If match
        print(f"\nYou got it! The answer was {number}.\n")    # Print win message
        return 0
    elif guess > number:    # If guess too high
        print(f"\n{guess} is too high. Try again.") # Tell user guess was too high
        return lives - 1  # Remove a life
    elif guess < number:    # If guess too low
        print(f"\n{guess} is too low. Try again.")  # Tell user guess was too low
        return lives - 1  # Remove a life

def game_level(choice):
    """Function used to set the game level and number of turns a user gets."""
    # Set level
    if choice == "easy":
        return 10  # Set lives to 10
    elif choice == "hard":
        return 5   # Set lives to 5
    else:   # If user enters anything else
        return 10  # Set lives to 10

def game():
    """Function to run the game."""
    level_choice = input("\nWhat level would you like to play? Easy or Hard? ") # Get level from user
    lives = game_level(level_choice)   # Set lives count by calling game_level function
    number = random.choice(range(1,101))  # Get random number

    clear() # Clear the console
    print(art.logo) # Print logo

    while lives >= 1: # While user has lives

        print(f"You have ({lives}) remaining to guess the number.") # Print updated lives count

        guess = input("\nMake a guess between 1 - 100: ")  # Get guess from user
        lives = check_guess(guess, lives, number)

print(art.logo) # Print logo
print("\nWelcome to Guess the Number!") # Print welcome message

game() # Call the game