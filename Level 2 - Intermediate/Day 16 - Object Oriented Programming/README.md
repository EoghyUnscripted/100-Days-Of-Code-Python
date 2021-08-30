# Day 16 Object-Oriented Programming

## Overview

Day 16 starts with reviewing Python classes and Object-Oriented Programming. Using this and what we have learned previously, we will work on Coffee Machine Part 2 where we will use classes and functions to recreate the original project from Day 15.

## Project: Coffee Machine Part 2

With the provided code from the course in the files `menu.py`, `coffee_maker.py`, and `money_machine.py`, we will focus on rebuilding our project using `classes` and `methods` to complete. The goal is the same as the previous day, but cleaner and more complex using objects.

### Instructions

1. Prompt user for drink type (espresso/latte/cappuccino)
2. Include a secret "off" prompt that will accept `OFF` as input for maintenance
3. Include a "report" prompt that will accept `REPORT` as input
   1. This will print the resource levels in the machine
   2. Will also allow machine to print the report when levels are too low for a drink
4. The program should check if the resources are sufficient for a drink selection
   1. If levels are too low, the program will output a message
   2. "Sorry, the water is too low."
5. Process coin payments
   1. Prompt user for coin counts to pay for drink
6. Check if payment successful
   1. Count the coins
      1. If amount greater than the cost of the drink, refund
      2. If too little, prompt for more change
   2. Add paid amount to a stored variable to count all payments
      1. Reduce amount by amount of change
7. Make Coffee
   1. Remove amount of each resource used to make the drink
   2. Print report with updated resources
   3. "Here is your drink! Enjoy!"
8. Prompt again for drink type

### Comments

As this project required not manipulating the provided code, it prevented me from handling input type exceptions. However, I was able to provide exceptions to keep the game running in the event that an input was invalid. For example, if the user entered the wrong command for drink or maintenance, it would ask again.

### Game Demo

[Replit Demo - Coffee Machine Part 2](https://replit.com/@EoghyUnscripted/Coffee-Machine-Part-2)