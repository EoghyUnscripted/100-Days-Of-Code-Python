"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 30
EXERCISE: 30-1 IndexError Handling
LEVEL: Intermediate

"""

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    
    try:    # Try to execute code
        fruit = fruits[index]
    except IndexError:  # If IndexError
        print("Fruit pie")  # Print default of Fruit pie
    else:   # If no error
        print(fruit + " pie")   # Print fruit at index + pie


make_pie(4) # Call function