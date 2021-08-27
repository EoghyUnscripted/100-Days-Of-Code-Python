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
    account = random.choice(game_data.data) # Gets random account
    return account

def check_account(A, B):
    """Function to check that the accounts are not the same."""
    if A == B:  # Checks if accounts are the same
        return True # If same
    else:
        return False    # If different

def get_message(account):
    """Function to generate a message from the account info passed as parameter."""
    message = account["name"] + ", a " + account["description"] + ", from " + account["country"] + "."  # Output message
    return message

def check_answer(A, B, guess):
    """Function to check the user guess against the correct answer."""
    
    answer = "" # Sets blank variable for answer

    if A["follower_count"] > B["follower_count"]:   # Checks if A has more followers than B
        answer = "A"    # If true, set answer to A
    elif B["follower_count"] > A["follower_count"]: # Checks if B has more followers than A
        answer = "B"    # If true, set answer to B

    if guess == answer: # Checks that user guessed right
        return True # If correct
    else:
        return False    # If wrong

def game():
    """Function for main gameplay."""

    print(art.logo) # Print logo
    print("\nWelcome to Higher or Lower!")  # Print welcome message

    continue_game = True # Set gameplay boolean
    score = 0   # Set initial score

    # Get initial account data
    account_A = get_account()   # Get random account for A
    account_B = get_account()   # Get random account for B
    message_A = get_message(account_A)  # Get message for A
    message_B = get_message(account_B)  # Get message for B

    while check_account(account_A, account_B):  # Checks if accounts are the same
        account_B = get_account()   # Get new random account for B
        message_B = get_message(account_B)  # Get new message for B

    while continue_game:    # While game is active

        print(f"\nCompare A: {message_A}\n")    # Print message A
        print(art.vs)   # Print VS art
        print(f"\nAgainst B: {message_B}\n")    # Print message B

        guess = input("Who has more followers on Instagram? A or B?: ").upper() # Get guess from user

        continue_game = check_answer(A=account_A, B=account_B, guess=guess) # Checks answer, ends game if wrong

        if continue_game:   # If right answer
            score += 1  # Add to score
            clear() # Clear console
            print(art.logo) # Print logo
            print(f"\nYou're right! Your current score is: {score}")    # Print response
            
            # Reset the accounts
            account_A = account_B   # Set account B to A
            message_A = message_B   # Set message B to A
            account_B = get_account()   # Get random account for B
            message_B = get_message(account_B)  # Get message for B

            while check_account(account_A, account_B):  # Checks if accounts are the same
                account_B = get_account()   # Get new random account for B
                message_B = get_message(account_B)  # Get new message for B
        else: # If wrong answer
            clear() # Clear console
            print(art.logo) # Print logo
            print(f"\nSorry, that is wrong. Your final score is: {score}\n")    # Print response

game()  # Call game