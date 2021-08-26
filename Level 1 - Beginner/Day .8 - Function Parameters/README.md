# Day 8 Function Parameters

## Overview

Day 8 starts with creating functions that take parameters when called to output results. From there we continue to use conditionals, loops, lists, and variables to build a Caesar Cipher.

    Exercise 8.1 - Build a function that would calculate how many paint cans are needed to cover a wall with user input heigh and width
    Exercise 8.2 - Build a function that accepts a user input number and checks if the number is prime with loops

The Caesar Cipher project is broken up into multiple layers that are added on as we progress. We begin with the basics by developing the functions and flow, to cleaning up the code to shorten and create reusable code.

    Project 8.1 - Start the project by building an encryption function that accepts user message input and outputs an encoded string
    Project 8.2 - Create a decode function that will accept an encoded user message input and outputs a decoded string
    Project 8.3 - Combine the two functions into one that will perform the option the user requests when the program starts and outputs the desired result

## Project: Caesar Cipher

Using what was learned from the project milestones, the final project for Day 8 was to build a completed Caesar Cipher program to code and decode messages. The completed program would include importing external modules for use in the game and a function that accepts parameter input, and outputs either an encoded or decoded message per user choice.

### Instructions

1. Import and print the logo from art.py when the program starts.

2. What if the user enters a shift that is greater than the number of letters in the alphabet?

    1. Try running the program and entering a shift number of 45.
    2. Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    3. Hint: Think about how you can use the modulus (%).

3. What happens if the user enters a number/symbol/space?
    1. Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

            e.g. start_text = "meet me at 3"
                 end_text = "•••• •• •• 3"

4. Can you figure out a way to ask the user if they want to restart the cipher program?

            e.g. Type 'yes' if you want to go again. Otherwise type 'no'.

    1. If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    2. Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

#### Code

Use the provided code to complete the project.

```python
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  ]

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # TODO What happens if the user enters a number/symbol/space?
    # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

# TODO Import and print the logo from art.py when the program starts.

# TODO Can you figure out a way to ask the user if they want to restart the cipher program? 

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO What if the user enters a shift that is greater than the number of letters in the alphabet?
#      Add some code so that the program continues to work even if the user enters a shift number greater than 26.

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
```

### Game Demo

[Replit Demo - Caesar Cipher](https://replit.com/@EoghyUnscripted/Caesar-Cipher)
