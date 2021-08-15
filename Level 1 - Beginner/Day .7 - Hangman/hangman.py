"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 7
PROJECT: HANGMAN
LEVEL: Beginner

INSTRUCTIONS:

    Using the code from 7-4, continue to add to the program for the final project.

    Step 1 - Update the word list to use the 'word_list' from hangman_words.py file.
    Step 2 - Import the stages from the hangman_art.py file.
    Step 3 - Import the logo from hangman_art.py and print it at the start of the game.
    Step 4 - If the user has entered a letter they've already guessed, print the letter and let them know.
    Step 5 - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

"""

import random
import Packages.hangman_words
import Packages.hangman_art

lives = 6   # Variable to track lives remaining in game

chosen_word = random.choice(Packages.hangman_words.word_list).upper() # Get a random word from the list

display = []    # Blank list to hold correct guesses
guess_list = [] # Blank list to store all guesses

for char in chosen_word:
    display.append("_") # Add blanks to display to user for guessing

print(Packages.hangman_art.logo)    # Print Logo at start of game

end_of_game = False # Sets initial condition for game status

while not end_of_game:  # Loops program until all blanks are filled

    guesses = ' '.join(guess_list).upper()
    print(Packages.hangman_art.stages[lives])    # Print ASCII in current stage
    print(f"\n{' '.join(display)}\n")
    print(f"Your guesses: {guesses}")
    guess = input("\nGuess a letter: ").upper() # Get letter input from user in lowercase

    if guess in guess_list:    # Check if user already guessed letter
        print(f"You have already guessed the letter \"{guess}\".")
    else:

        guess_list.append(guess)   # Add letter to guess list

        for position in range(len(chosen_word)): # Loop through each position index
            letter = chosen_word[position] # Get letter in random word position
            if letter == guess: # Checks if guess matches letter
                display[position] = guess   # Adds to display list in same position if matches
        
        if guess not in chosen_word:    # Checks if guess is not in word
            lives -= 1  # Subtract 1 life
            if lives == 0:    # If no lives remain
                end_of_game = True  # Set end of game to True
                print(Packages.hangman_art.stages[lives])    # Print ASCII in current stage
                print(f"\n{' '.join(display)}\n")
                print("\nYou lose!\n")
                exit()  # Stop program
            elif lives > 0: # If there are still lives remaining
                print(f"\nThe letter \"{guess}\" is not in the word.\n")
            
    print(f"\n{' '.join(display)}\n")

    if "_" not in display:  # Checks if blanks are filled
        end_of_game = True  # Set end of game as True
        print("\nYou win!\n")