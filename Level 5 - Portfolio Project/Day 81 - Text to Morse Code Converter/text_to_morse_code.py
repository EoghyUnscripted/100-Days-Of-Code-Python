"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 81
PROJECT: Text To Morse Code Converter
LEVEL: Portfolio Project

"""

import os
from Art import logo as l
from Data import morse_code as mc


logo = l.logo
morse = mc.morse_code

endgame = False

while not endgame:
    
    os.system('clear')

    print(logo)
    
    morse_string = ""

    user_string = input(f"Please type a string to be converted: \n").lower()

    for letter in user_string:
        
        if letter == " ":
            morse_string += "   "
        elif morse[letter]:
            morse_string += (morse[letter] + " ")
        else:
            continue

    print(f"\n {morse_string} \n")
    
    user_choice = input(f"Would you like to convert another string? Y/N: ").lower()
    
    if user_choice == "n":
        endgame = True
        