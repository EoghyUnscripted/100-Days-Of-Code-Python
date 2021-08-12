"""
INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

"""

# DAY: 1
# EXERCISE: BAND NAME GENERATOR ADVANCED CODING

# INSTRUCTIONS:

# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

def Generator(city, pet):

    band_Name = "Your band name could be " + city + " " + pet + "."
    
    return print(band_Name)

print("Welcome to the Band Name Generator.")
city = input("What city did you grow up in?\n")
pet = input("What is your pets name?\n")

Generator(city, pet)