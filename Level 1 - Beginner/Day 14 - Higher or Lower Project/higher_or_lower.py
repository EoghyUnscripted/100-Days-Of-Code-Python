"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 14
PROJECT: Higher or Lower
LEVEL: Beginner

"""

from Modules import art, game_data
import random
import os

def clear():
    """Function used to clear the console."""
    os.system('clear') #on Linux System

def get_account():
    """Function to generate a random account from the data file."""
    account = random.choice(game_data.data)
    return account

def get_message(account):
    """Function to generate a message from the account info passed as parameter."""
    message = account["name"] + ", a " + account["description"] + ", from " + account["country"] + "."
    return message

def check_answer(A, B, guess):
    """Function to check the user guess against the correct answer."""
    
    answer = ""

    if A["follower_count"] > B["follower_count"]:
        answer = "A"
    elif B["follower_count"] > A["follower_count"]:
        answer = "B"

    if guess == answer:
        return True
    else:
        return False

def game():

    print(art.logo)
    print("\nWelcome to Higher or Lower!")

    continue_game = True # Set gameplay boolean
    score = 0   # Set initial score

    # Get initial account data
    account_A = get_account()   # Get random account for A
    message_A = get_message(account_A)  # Get message for A
    account_B = get_account()   # Get random account for B
    message_B = get_message(account_B)  # Get message for B

    while continue_game:

        print(f"\nCompare A: {message_A}\n")
        print(art.vs)
        print(f"\nAgainst B: {message_B}\n")

        guess = input("Who has more followers on Instagram? A or B?: ").upper()

        continue_game = check_answer(A=account_A, B=account_B, guess=guess)

        if continue_game:
            score += 1
            clear()
            print(art.logo)
            print(f"\nYou're right! Your current score is: {score}")
            
            # Reset the accounts
            account_A = account_B   # Set account B to A
            message_A = message_B   # Set message B to A
            account_B = get_account()   # Get random account for B
            message_B = get_message(account_B)  # Get message for B
        else:
            clear()
            print(art.logo)
            print(f"\nSorry, that is wrong. Your final score is: {score}\n")

game()