"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 4
PROJECT: ROCK, PAPER, SCISSORS

INSTRUCTIONS:

    Create a program that allows you to select Rock, Paper, or Scissors.
    When you input the selection, the program will randomly select a choice as well.

    The game compares each choice and determines the winner based on the official rules.

    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock

"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors\nWhat will you pick: Rock, Paper or Scissors?")

userChoice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
compChoice = random.randint(0,2)

# Check if tied
if userChoice == compChoice:
    if userChoice == 0:
        print(f"\nYou picked Rock \n{rock}")
        print(f"\nThe computer picked Rock \n{rock}")
        print("\nIt's a tie!")
        exit
    elif userChoice == 1:
        print(f"\nYou picked Paper \n{paper}")
        print(f"\nThe computer picked Paper \n{paper}")
        print("\nIt's a tie!")
        exit
    elif userChoice == 2:
        print(f"\nYou picked Scissors \n{scissors}")
        print(f"\nThe computer picked Scissors \n{scissors}")
        print("\nIt's a tie!")
        exit

# If not tied
if userChoice == 0:
    if compChoice == 1:
        print(f"\nYou picked Rock \n{rock}")
        print(f"\nThe computer picked Paper \n{paper}")
        print("\nYou Lose!")
    if compChoice == 2:
        print(f"\nYou picked Rock \n{rock}")
        print(f"\nThe computer picked Scissors \n{scissors}")
        print("\nYou Win!")
elif userChoice == 1:
    if compChoice == 0:
        print(f"\nYou picked Paper \n{paper}")
        print(f"\nThe computer picked Rock \n{rock}")
        print("\nYou Win!")
    if compChoice == 2:
        print(f"\nYou picked Paper \n{rock}")
        print(f"\nThe computer picked Scissors \n{scissors}")
        print("\nYou Lose!")
elif userChoice == 2:
    if compChoice == 0:
        print(f"\nYou picked Scissors \n{scissors}")
        print(f"\nThe computer picked Rock \n{rock}")
        print("\nYou Lose!")
    if compChoice == 1:
        print(f"\nYou picked Scissors \n{scissors}")
        print(f"\nThe computer picked Paper \n{paper}")
        print("\nYou Win!")