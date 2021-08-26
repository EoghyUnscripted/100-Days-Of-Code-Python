# Day 7 Hangman

## Overview

Day 7 starts with using the `choice()` function to pick random words from a list. From there we move into working more with lists and tracking user input and scores during gameplay.

    Project 7.1 - Work with the choice() function to have program pick a random word, test user input letters if in the word
    Project 7.2 - Updating an empty list with correct letter guesses in placement of the letters in the word
    Project 7.3 - Keeping track of user progress by testing the list for remaining blanks
    Project 7.4 - Tracking user lives left in the game

## Project: Hangman Game

Using what was learned from the project milestones, the final project for Day 7 was to build a completed Hangman Game. The completed game would include importing external modules for use in the game. The final project would also track if user has already guessed a letter and alert them.

### Instructions

Using the code from 7-1 to 7-4, continue to add final touches to the program for the final project.

1. Update the word list to use the 'word_list' from hangman_words.py file.

2. Import the stages from the hangman_art.py file.

3. Import the logo from hangman_art.py and print it at the start of the game.

4. If the user has entered a letter they've already guessed, print the letter and let them know.

5. If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

   1. The course instructions say to subtract a life from the user, but I chose to allow the user to guess again.

   2. In the next iteration, I will update the stages ASCII to allow for more lives as I would do when I was a kid.

#### Code

```python
import random

# TODO Update the word list to use the 'word_list' from hangman_words.py
#      Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO Import the logo from hangman_art.py and print it at the start of the game.

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # TODO If the user has entered a letter they've already guessed, print the letter and let them know.

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO Import the stages from hangman_art.py.
    print(stages[lives])
```

### Game Demo

[Replit Demo - Hangman](https://replit.com/@EoghyUnscripted/Hangman)
