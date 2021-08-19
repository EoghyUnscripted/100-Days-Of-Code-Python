"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 7
PROJECT: 7-2 Hangman: Replacing Blanks with Guesses
LEVEL: Beginner

"""

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list) # Get a random word from the list

display = []    # Blank list to hold guesses

for char in chosen_word:
    display.append("_") # Add blanks to display to user for guessing

print(display)  # Print display for user

guess = input("Guess a letter: ").lower() # Get letter input from user in lowercase

for position in range(len(chosen_word)): # Loop through each position index
    letter = chosen_word[position] # Get letter in random word position
    if letter == guess: # Checks if guess matches letter
        display[position] = guess   # Adds to display list in same position if matches

print(display)