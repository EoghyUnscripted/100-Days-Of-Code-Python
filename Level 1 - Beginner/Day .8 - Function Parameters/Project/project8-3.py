"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 8
PROJECT: 8-3 Caesar Cipher: Reorganising the Code
LEVEL: Beginner

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
recoded = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, message, word_shift):

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

        location = alphabet.index(char) # Get location from original alphabet 
        caesar_letter = recoded[location]     # Get letter from shifted alphabet
        caesar_text += caesar_letter  # Add to output text variable

    print(f"The {direction}d text is {caesar_text}")

caesar(direction=direction, message=text, word_shift=shift) # Call function