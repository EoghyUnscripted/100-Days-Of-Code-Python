"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 4
EXERCISE: 4-3 Treasure Map

"""

# Set mapping lists
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# Combine lists
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")  # Print Treasure Map

position = input("Where do you want to put the treasure? ") # Get coordinates from user

x = int(position[0])  # Set X
y = int(position[1])  # Set Y

map[y - 1][x - 1] = 'X' # Update Treasure Map input

print(f"{row1}\n{row2}\n{row3}")  # Print new map