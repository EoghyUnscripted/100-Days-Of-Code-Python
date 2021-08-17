"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 8
PROJECT: Caesar Cipher
LEVEL: Beginner

INSTRUCTIONS:

    1. Import and print the logo from art.py when the program starts.
    2. What if the user enters a shift that is greater than the number of letters in the alphabet?
        i. Try running the program and entering a shift number of 45.
        ii. Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
        iii. Hint: Think about how you can use the modulus (%).
    3. What happens if the user enters a number/symbol/space?
        i. Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
            e.g. start_text = "meet me at 3" end_text = "•••• •• •• 3"
    4. Can you figure out a way to ask the user if they want to restart the cipher program?
            e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
        i. If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
        ii. Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

COMMENTS:

    I added the uppercase alphabet, digits, and common special characters to enhance the program.
    If user adds extra elements to the text, it will just copy them to the output string.
    While I could have settled with going the simple route that the instructor took when reviewing,
    I chose to stick with the list because it would allow me to use list functions to manipulate.

"""

from Packages.art import logo
from Packages.data import alphabet

def caesar(direction, message, word_shift):

    recoded = []    # Blank list for shifted alphabet

    # Copy elements from alphabet list to shifted list
    # Required to 'reset' list every time program loops
    for c in alphabet:
        recoded.append(c)

    caesar_text = ""   # Holds the output string

    # Shifts the letter placements in the recoded list
    for i in range(0, word_shift):
    
        if direction == "encode":
            recoded.append(recoded[0])  # Add element at beginning of list to the end
            recoded.pop(0)  # Remove element at beginning of list

        elif direction == "decode":
            last_elem = -1  # Variable pointing to last element in the list
            recoded.insert(0, recoded[last_elem])   # Get last item in the list and insert into first position
            recoded.pop(last_elem)  # Remove element at end of list

    # Loop through each character of the input text
    for char in message:
        # Checks if char is in the alphabet list
        if char in alphabet:
            location = alphabet.index(char) # Get location from original alphabet 
            caesar_letter = recoded[location]     # Get letter from shifted alphabet
            caesar_text += caesar_letter  # Add to output text variable
        else:   # If char not in alphabet list
            caesar_text += char  # Add input character to output text variable

    print(f"The {direction}d text is: {caesar_text}")

repeat = True
print(logo)

while repeat == True: # While user wants to keep restarting
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")    # Get Encode or Decode option from user
    text = input("\nType your message:\n")  # Get message to encode or decode from user
    shift = int(input("\nType the shift number:\n"))    # Get shift count from user

    caesar(direction=direction, message=text, word_shift=shift) # Call function

    # Ask if user wants to restart the cipher program
    run_again = input(f"\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    # Check response
    if run_again == "yes":
        # If yes
        repeat = True
    else:
        # If no
        repeat = False