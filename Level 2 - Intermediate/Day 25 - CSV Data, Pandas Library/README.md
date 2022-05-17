# Day 25 CSV Data, Pandas Library

## Overview

For Day 25, we will start with some exercises to learn how to work with Pandas and csv file data for weather and squirrel census data. The goal is to pull in the data using the Pandas library and use it within our program.

      Exercise 25.1 - Read file content and use the data for mathematical functions
      Exercise 25.2 - Read file content and use built-in functions and conditionals to output analysis results

## Project: U.S. States Game

Using the provided `50_states.csv` file, we will create a game to test how many states a user can guess on the map. The game will use the data file during gameplay to validate answers and lable the states on the map using coordinates within the file.

### Instructions

1. Create the Screen environment and load the US Map image onto the background
2. Create a prompt that accepts user input to guess a state name
3. Validate the input by:
   1. Accepting upper and lowercase input
   2. Matching against a state name in the provided csv file
4. If the user is correct:
   1. Get the coordinates from the file
   2. Write the state name on the map at the coordinates
5. Loop prompt until the count reaches 50
   1. Display current correct guesses / 50 on screen title
6. Write an exit code that will:
   1. Break the gameplay loop
   2. Write the names of the states user did not guess into a csv file

### Example Output

![US States Game 1](Images/us_states_game_1.png)
![US States Game 2](Images/us_states_game_2.png)

`states_to_learn.csv`

      ,state
      0,Arkansas
      1,Wisconsin

### Comments

There are two versions of the game in the main directory:

- us_states_game.py
- us_states_game_adj.py

Either file is possible to use within your preferred editor. The only difference is that `us_states_game_adj.py` is modified to accept terminal input instead of an on screen prompt.

#### Demo Notes

In an attempt to host this app on Replit, it became clear that, while Pandas can be installed using the package manager, none of the existing packages function to allow importing pandas for use in the app.
