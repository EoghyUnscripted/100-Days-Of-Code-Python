"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 7
EXERCISE: 7-2 Hangman: Replacing Blanks with Guesses
LEVEL: Beginner

INSTRUCTIONS:

    Using the code from 7-1, continue to add to the program for part 2.

    Step 1 - Create an empty List called display. 
             For each letter in the chosen_word, add a "_" to 'display'.
             So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] 
             with 5 "_" representing each letter to guess.
    Step 2 - Loop through each position in the chosen_word.
             If the letter at that position matches 'guess' then reveal that letter in the display at that position.
             e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    Step 3 - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

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