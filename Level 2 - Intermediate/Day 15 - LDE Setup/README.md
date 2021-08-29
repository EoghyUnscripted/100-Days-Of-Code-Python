# Day 15 Local Development Environment Setup

## Overview

Day 15 starts with learning how to set up Python 3 and PyCharm on our computers. For the sake of experience and organization, I chose to work with PyCharm instead of Visual Studio Code to gain some exposure to the development environment and tools. 

## Project: Coffee Machine Part 1

Using what we have learned in the beginner courses, we will build a program for a coffee machine similar to one you would find in a hospital. The program will allow users to choose a drink, pay for it using input prompts to enter coin counts, and the coffee machine will dispense the drink.

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

### Game Demo

[]()