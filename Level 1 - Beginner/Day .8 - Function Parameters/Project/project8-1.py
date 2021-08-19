"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 8
PROJECT: 8-1 Caesar Cipher: Encryption
LEVEL: Beginner

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, word_shift):

    enc_text = ""   # Holds the encrypted string

    # Loop through each character of the input text
    for char in message:

        # Gets the alphabet list index location of the character
        location = alphabet.index(char)

        # Tests if the shift input is greater than the range available
        if word_shift > len(alphabet):
            print(f"Please choose a number between 1 and {len(alphabet)}.")
            exit()  # Exits the program
        
        # Determines last avail position that can shift within range of list
        cycle = len(alphabet) - word_shift

        # If position is greater than last avail position that can shift
        if location > cycle:
            # Reset to beginning of list to continue shifting
            location -= len(alphabet)

        new_location = location + word_shift    # Get new position index number
        enc_letter = alphabet[new_location]     # Get letter from new index
        enc_text += enc_letter  # Add to encrypted text variable

    print(f"The encoded text is {enc_text}")

encrypt(message=text, word_shift=shift) # Call function to encrypt