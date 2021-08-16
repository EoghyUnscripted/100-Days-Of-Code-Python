# Day 7 Hangman Project

## Project 7-1: Picking a Random Word and Checking Answers

### Instructions

Step 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
Step 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
Step 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

Use the code provided -- do not change the existing code!

CODE:

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

Step 1 - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
         
         e.g. If the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

Step 2 - Loop through each position in the chosen_word. If the letter at that position matches 'guess' then reveal that letter in the display at that position.
            
            e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

Step 3 - Print `display` and you should see the guessed letter in the correct position and every other letter replace with "_".

### Example Input

Pssst, the solution is aardvark.

    ['_', '_', '_', '_', '_', '_', '_', '_']

    Guess a letter: a

### Example Output

    ['a', 'a', '_', '_', '_', 'a', '_', '_']

## Project 7-1: Picking a Random Word and Checking Answers

### Instructions

Step 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
Step 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
Step 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

Use the code provided -- do not change the existing code!

CODE:

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

## Project 7-1: Picking a Random Word and Checking Answers

### Instructions

Step 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
Step 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
Step 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

Use the code provided -- do not change the existing code!

CODE:

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