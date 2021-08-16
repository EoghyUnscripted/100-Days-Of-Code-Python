"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 7
PROJECT: 7-3 Hangman: Checking If User Has Won
LEVEL: Beginner

INSTRUCTIONS:

    Using the code from 7-2, continue to add to the program for part 3.

    Step 1 - Use a while loop to let the user guess again. The loop should only 
             stop once the user has guessed all the letters in the chosen_word and 
             'display' has no more blanks ("_"). 
             Then you can tell the user they've won.

"""

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list) # Get a random word from the list

display = []    # Blank list to hold guesses

for char in chosen_word:
    display.append("_") # Add blanks to display to user for guessing

print(display)

end_of_game = False # Sets initial condition for game status

while not end_of_game:  # Loops program until all blanks are filled

    guess = input("Guess a letter: ").lower() # Get letter input from user in lowercase

    for position in range(len(chosen_word)): # Loop through each position index
        letter = chosen_word[position] # Get letter in random word position
        if letter == guess: # Checks if guess matches letter
            display[position] = guess   # Adds to display list in same position if matches

    print(display)

    if "_" not in display:  # Checks if blanks are filled
        end_of_game = True  # Set end of game as True
        print("You win!")