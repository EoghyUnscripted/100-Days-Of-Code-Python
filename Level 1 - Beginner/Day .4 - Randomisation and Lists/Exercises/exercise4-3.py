"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 4
EXERCISE: 4-3 Treasure Map
LEVEL: Beginner

INSTRUCTIONS:

    Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
    The first digit is the vertical column number and the second digit is the horizontal row number.

    column 2, row 3 would be entered as: 23

    Output:

      ['⬜️', '⬜️', '⬜️']

      ['⬜️', '⬜️', '⬜️']

      ['⬜️', 'X', '⬜️']

    Use the code provided -- do not change the existing code!

    CODE:

      row1 = ["⬜️","⬜️","⬜️"]
      row2 = ["⬜️","⬜️","⬜️"]
      row3 = ["⬜️","⬜️","⬜️"]
      map = [row1, row2, row3]
      print(f"{row1}\n{row2}\n{row3}")
      position = input("Where do you want to put the treasure? ")

      # WRITE YOUR CODE HERE

      print(f"{row1}\n{row2}\n{row3}")

"""

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x = int(position[0])
y = int(position[1])
map[y - 1][x - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")