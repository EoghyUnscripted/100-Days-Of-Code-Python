"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 7
PROJECT: 7-1 Hangman: Picking a Random Word and Checking Answers
LEVEL: Beginner

"""

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)  # Get a random word from list

guess = input("Guess a letter: ").lower() # Get letter input from user in lowercase

for letter in chosen_word:
    if letter == guess: # Check if letter is in the random word
        print("Right")
    else:   # If letter is not in the random word
        print("Wrong")