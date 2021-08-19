# Day 5 Loops

## Overview

Day 5 starts with using FOR, and IF loops, including the `range()` function to cycle through lists.

    Exercise 5.1 - Calculate the average height from a user input list of numbers
    Exercise 5.2 - Calculate the highest score from a user input list of numbers
    Exercise 5.3 - Loop through even numbers and sum them
    Exercise 5.4 - Loop through numbers and calculate if divisible by 3, 5, or both and output Fizz, Buzz, or FizzBuzz

## Project: Password Generator

Using what was learned from the exercises, the project for Day 5 was to build a Password Generator app. The app would ask the user how many letters, numbers, and symbols that they want and output a password for the user.

### Instructions

Create a program that accepts input for count of letters, numbers and symbols.
The program will use pre-existing lists to randomly select from each to generate a password.

Easy Level: Cycle sequentially through letters, numbers then symbols to create a password

    hsjE32#$

Hard Level: Cycle randomly through letters, numbers then symbols to create a password

    0$nD3@ca

#### Code

Use the provided code to complete the program.

```python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# WRITE YOUR CODE HERE
```
