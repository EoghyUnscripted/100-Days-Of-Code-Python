"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 7
EXERCISE: 7-4 Hangman: Tracking Players' Lives Remaining
LEVEL: Beginner

INSTRUCTIONS:

    Using the code from 7-3, continue to add to the program for part 4.

    Step 1 - Create a variable called 'lives' to keep track of the number of lives left. 
             Set 'lives' to equal 6.
    
    Step 2 - If guess is not a letter in the chosen_word,
             Then reduce 'lives' by 1. 
             If lives goes down to 0 then the game should stop and it should print "You lose."

    Step 3 - Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

"""

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6   # Variable to track lives remaining in game

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list) # Get a random word from the list

display = []    # Blank list to hold guesses

for char in chosen_word:
    display.append("_") # Add blanks to display to user for guessing

print(f"\n{' '.join(display)}\n")

end_of_game = False # Sets initial condition for game status

while not end_of_game:  # Loops program until all blanks are filled

    print(stages[lives])    # Print ASCII in current stage
    guess = input("\nGuess a letter: ").lower() # Get letter input from user in lowercase

    for position in range(len(chosen_word)): # Loop through each position index
        letter = chosen_word[position] # Get letter in random word position
        if letter == guess: # Checks if guess matches letter
            display[position] = guess   # Adds to display list in same position if matches
    
    if guess not in chosen_word:    # Checks if guess is not in word
        lives -= 1
        if lives == 0:    # If no lives remain
            end_of_game = True  # Set end of game to True
            print(stages[lives])    # Print ASCII in current stage
            print(f"\n{' '.join(display)}\n")
            print("\nYou lose!\n")
            exit()
        elif lives > 0:
            print("\nThat letter is not in the word.\n")
            
    print(f"\n{' '.join(display)}\n")

    if "_" not in display:  # Checks if blanks are filled
        end_of_game = True  # Set end of game as True
        print("\nYou win!\n")