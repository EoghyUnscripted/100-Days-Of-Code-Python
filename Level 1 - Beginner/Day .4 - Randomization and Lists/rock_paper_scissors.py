"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 4
PROJECT: ROCK, PAPER, SCISSORS
LEVEL: BEGINNER

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

# Check if user input is valid
if userChoice < 0 or userChoice > 2:
    print("That is an invalid choice, you lose!")
    exit()

art = [rock, paper, scissors]
text = ["Rock", "Paper", "Scissors"]

print(f"\nYou picked {text[userChoice]}:\n{art[userChoice]}\n")
print(f"\nComputer picked {text[compChoice]}:\n{art[compChoice]}\n")

# Check if tied
if userChoice == compChoice:
    print("\nIt's a tie!")
    exit()

# If not tied
if userChoice == 0:
    if compChoice == 1:
        print("Paper covers rock, you lose!")
    elif compChoice == 2:
        print("Rock breaks scissors, you win!")
elif userChoice == 1:
    if compChoice == 0:
        print("Paper covers rock, you win!")
    elif compChoice == 2:
        print("Scissors cut paper, you lose!")
elif userChoice == 2:
    if compChoice == 0:
        print("Rock beats scissors, you lose!")
    elif compChoice == 1:
        print("Scissors cut paper, you win!")