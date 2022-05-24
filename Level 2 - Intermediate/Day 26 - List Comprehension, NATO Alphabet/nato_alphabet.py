"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 26
PROJECT: NATO Alphabet
LEVEL: Intermediate

"""

import pandas

# Get data from the provided csv file
data = pandas.read_csv("Modules/nato_phonetic_alphabet.csv")
print(data.to_dict())

# Loop through rows of a data frame
nato_dict = {column.letter: column.code for (row, column) in data.iterrows()}

print(nato_dict["A"])

conversion_string = input("Enter a word to convert to NATO alphabet: ").upper()     # Get user input

# Convert to NATO in a list
nato_output = [nato_dict[letter] for letter in conversion_string]

print(nato_output)