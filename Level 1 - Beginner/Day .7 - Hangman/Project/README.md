# Day 7 Hangman Project

## Project 7-1: Picking a Random Word and Checking Answers

### Instructions

1. Randomly choose a word from the word_list and assign it to a variable called chosen_word.

2. Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

3. Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

***Use the code provided -- do not change the existing code!***

    word_list = ["aardvark", "baboon", "camel"]

    # WRITE YOUR CODE HERE


### Example Input

The program will choose a random word and the user will need to guess the letters in the word.

The random word chosen was **baboon**:

    Guess a letter: a

### Example Output

With each guess, the program will check if the letter is in the word or not and print `Right` or `Wrong`.

    Wrong
    Right
    Wrong
    Wrong
    Wrong
    Wrong

## Project 7-2: Replacing Blanks with Guesses

### Instructions

Using the code from 7-1, continue to add to the program for part 2.

1. Create an empty List called display. For each letter in the chosen_word, add a "\_" to 'display'.
   e.g. If the chosen_word was "apple", display should be `["_", "_", "_", "_", "_"]` with 5 "\_" representing each letter to guess.

2. Loop through each position in the chosen_word. If the letter at that position matches 'guess' then reveal that letter in the display at that position.
   e.g. If the user guessed "p" and the chosen word was "apple", then display should be `["_", "p", "p", "_", "_"]`.

3. Print `display` and you should see the guessed letter in the correct position and every other letter replace with "\_".

### Example Input

Pssst, the solution is aardvark.

    ['_', '_', '_', '_', '_', '_', '_', '_']

    Guess a letter: a

### Example Output

    ['a', 'a', '_', '_', '_', 'a', '_', '_']

## Project 7-3: Checking If User Has Won

### Instructions

Using the code from 7-2, continue to add to the program for part 3.

1. Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 
   `display` has no more blanks ("_"). Then you can tell the user they've won.

### Example Input

    Pssst, the solution is baboon.
    Guess a letter: j

### Example Output

J is not in the word so the output shows:

    ['_', '_', '_', '_', '_', '_']

### Example Run

Pssst, the solution is baboon.

    Guess a letter: j
    ['_', '_', '_', '_', '_', '_']

    Guess a letter: n
    ['_', '_', '_', '_', '_', 'n']

    Guess a letter: k
    ['_', '_', '_', '_', '_', 'n']

    Guess a letter: r
    ['_', '_', '_', '_', '_', 'n']

    Guess a letter: i
    ['_', '_', '_', '_', '_', 'n']

    Guess a letter: p
    ['_', '_', '_', '_', '_', 'n']

    Guess a letter: o
    ['_', '_', '_', 'o', 'o', 'n']

    Guess a letter: b
    ['b', '_', 'b', 'o', 'o', 'n']

    Guess a letter: a
    ['b', 'a', 'b', 'o', 'o', 'n']

    You win!

## Project 7-4: Tracking Players' Lives Remaining

### Instructions

Using the code from 7-3, continue to add to the program for part 4.

1. Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
    
2. If `guess` is not a letter in the chosen_word, then reduce `lives` by 1. 
   If lives goes down to 0, then the game should stop and it should print "You lose."

3. Print the provided ASCII art from `stages` that corresponds to the current number of `lives` the user has remaining.

### Example Input 1

    _ _ _ _ _ _

    +---+
    |   |
        |
        |
        |
        |
    =========

    Guess a letter: a

### Example Output 1

    _ a _ _ _ _

    +---+
    |   |
        |
        |
        |
        |
    =========

    Guess a letter: 

### Example Input 2

    _ a _ _ _ _

    +---+
    |   |
        |
        |
        |
        |
    =========

    Guess a letter: r

### Example Output 2

    That letter is not in the word.

    _ a _ _ _ _

    +---+
    |   |
    O   |
        |
        |
        |
    =========

    Guess a letter: 