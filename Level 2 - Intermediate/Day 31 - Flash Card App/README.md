# Day 31 Flash Card App

## Overview

For Day 31, we will be completing a Flash Car App for the final project of this section.

## Project: Flash Card App

Using the images from the starting file and what we have learned with Tkinter, we will build a user interface to display flash cards in a foreign language. The cards will flip and show us the English translation.

### Instructions

1. Create the user interface with Tkinter
   1. Window:
      1. Padding - 50px
   2. Canvas:
      1. Height = 526, Width = 800
      2. 2x2 Grid
   3. Flash Cards:
      1. Span 2 columns
      2. Grid 0,0
      3. Title
         1. x=400, y=150
         2. Arial, 40, italic
      4. Word
         1. x=400, y=263
         2. Arial, 60, bold
      5. Buttons
         1. Wrong - Grid 0,1
         2. Right - Grid 1,1
2. Create the flash cards
   1. Write a function that:
      1. Gets a random foreign word from the `translations.csv` file using Pandas
      2. Updates to the new word on the flash card
3. Flip the card
   1. Write a function that:
      1. "Flips" the card to show the `card_back.png` image
      2. Changes the title to `English`
      3. Changed the word to the English translation
4. Save your progress
   1. Create a function that:
      1. Removes the current translation from the word list when user clicks the `check` button
      2. Saves the remaining words to a `words_to_learn.csv` file to be used moving forward
   2. Write exception handling for:
      1. `FileNotFoundError`
         1. If the words to learn file does not exist, it will use `translations.csv` instead

### Example Input

![Flash Cards App 1](Level 2 - Intermediate/Day 31 - Flash Card App/Images/flash_cards_app1.png)

#### translations.csv

```csv
portuguese,english
que,what
não,no
de,in
você,you
eu,I
um,a
para,for
se,if
está,it is
uma,one
com,with
me,me
por,per
ele,he
isso,this
em,in
do,of
bem,good
mas,but
como,how
da,gives
os,you
no,at the
aqui,on here
na,at
...
```

### Example Output

![Flash Cards App 2](Level 2 - Intermediate/Day 31 - Flash Card App/Images/flash_cards_app2.png)

#### words_to_learn.csv

```csv
portuguese,english
que,what
não,no
de,in
você,you
eu,I
um,a
para,for
se,if
está,it is
uma,one
com,with
me,me
por,per
ele,he
isso,this
em,in
do,of
bem,good
mas,but
como,how
da,gives
os,you
no,at the
aqui,on here
na,at
...
```

### Comments

For this application, I chose to go with Portuguese instead of French as the course instructed. I followed the resources given to get a list of most commonly used words in Portugues and translated them for the `translations.csv` file. You can replace this file with your own translations if you wish, or just use the included file.

Personally, I hate using global variables and would normally pass them through the function parameters. However, with Tkinter button commands, it doesn't make it easy to do. If you want a challenge, see if you can come up with a way to do this.

This concludes the `intermediate` section of my 100 days of Python challenge.

#### Demo Notes

Tkinter is not supported on Replit and has no demo available.
