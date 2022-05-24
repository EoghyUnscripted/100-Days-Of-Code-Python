"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 30
EXERCISE: 30-3 Exception Handling with the NATO Alphabet Project
LEVEL: Intermediate

"""

import pandas

data = pandas.read_csv("Level 2 - Intermediate/Day 30 - Errors, Exceptions, JSON Data/Exercises/Input/exercise30-3.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def convert():
    """ Function used to get user input and convert to NATO Phonetic Alphabet. """
    
    word = input("Enter a word: ").upper()  # Ask user for input

    try:    # Try to convert to NATO Phonetic Alphabet
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:    # On KeyError
        print("Only letters in the alphabet are allowed.")  # Alert user to only use alphabetical letters
        convert()   # Recursive function call to repeat user input until correct
    else:
        print(output_list)  # Print the conversion to console when no errors
        
convert()   # Call conversion function
