# Day 24 Files, Directories, and Paths

## Overview

For Day 24, we will be enhancing the Snake Game from day 21 and changing the scoreboard to use a file for tracking new high scores during gameplay. After, we will build a Mail Merge project.

      Exercise 24.1 - Rewrite the Snake Game scoreboard to store highest score of all time

## Project: Mail Merge

Using the provided files and folder hierarchy, we will be creating birthday invites. There is a file with a list of names and a template invite that we will be using to create a personalized letter for each name on the invite list.

- Input
  - Letters
    - starting_letter.txt
  - Names
    - invited_names.txt
- Output
  - ReadyToSend
    - letter_for_NAME1.txt
    - letter_for_NAME2.txt
    - etc.

### Instructions

1. Create a letter using starting_letter.txt
2. For each name in invited_names.txt
   1. Replace [name] in the created letter with the person's name
   2. Save the personalized letter to the "ReadyToSend" folder

### Example Input

#### starting_letter.txt

```
Dear [name],

You are invited to my birthday this Saturday.

The party will be at 1pm at my house.

Hope you can make it!

Eoghy

```

#### invited_names.txt

```
John
Kevin
Clara
Yogi
Michelle
Paul
Sarah
Anapaula
```

### Example Output

#### example.txt

      Dear John,

      You are invited to my birthday this Saturday.

      The party will be at 1pm at my house.

      Hope you can make it!

      Eoghy

### Comments

Personally, I chose to push all the functions into a separate file for this project. The primary reason being that it felt bulky. However, I wanted to make sure that the functions were somewhat re-usable and clearly documented. For example, I can change the file paths with ease and use the same functions to get the same output using different data. I prefer his approach when developing as it avoids wasted time re-writing code and requiring the need to modify existing code when scaling.

#### Demo Notes

As this program is all backend processing, there is no demo version available on Replit.
