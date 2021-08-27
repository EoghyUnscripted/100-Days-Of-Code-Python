"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 11
PROJECT: Blackjack
LEVEL: Beginner

"""

from Modules import art
import random
import os

def clear():
    """Function used to clear the console."""
    os.system('clear') #on Linux System

print(art.logo) # Import logo
print('Welcome to Blackjack!')  # Welcome message

start_game = input("Do you want to play a game of Blackjack? Y or N: ").lower() # Prompt user to start game

def blackjack(start):
    """Function with parameter to determine if Blackjack game should start or quit. Contains gameplay programming."""

    start_game = start  # Assigns function parameter to variable
    continue_game = True

    if start_game == "n":   # If user does not want to play
        return  # Stops the program

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    # List of cards to deal
    user_cards = [] # Stores dealt cards for user
    dealer_cards = []   # Stores dealt cards for dealer

    def deal_cards(cards_list):
        """Function to randomly select a card from the list and add to the player hand."""
        cards_list.append(random.choice(cards)) # Return index

    def compare(user, dealer):
        """Function used to compare scores of the user hand and computer hand to determine a winner."""

        user_score = get_score(user)    # Get updated user score
        dealer_score = get_score(dealer)    # Get updated dealer score

        # Check for Blackjacks
        if user_score == 0:
            return "You have a Blackjack! You win!"
        elif dealer_score == 0:
            return "Dealer has a Blackjack! You lose."

        if user_score > 21 and dealer_score > 21:
            # If both scores are over 21
            return "Both players went over 21. No winner."
        elif dealer_score > 21:
            # If dealer score is over 21
            return "Dealer went over 21. You win!"
        elif user_score > 21:
            # If user score is over 21
            return "You went over 21. You lose."
        elif user_score > dealer_score:
            # If user score is greater than dealer score
            return "You win!"
        elif dealer_score > user_score:
            # If dealer score is greater than user score
            return "Dealer wins!"
        else:
            # Any other outcome
            return "No winner."

    def get_score(hand):
        """Function used to calculate current scores using a list that is passed as a parameter."""

        if sum(hand) == 21 and len(hand) == 2:
            return 0
        elif 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
            return sum(hand)
        elif sum(hand) > 21:
            score = sum(hand)
            continue_game = False
        else:
            score = sum(hand)

        return sum(hand)

    for _ in range(2):    # Deals first round of cards
        deal_cards(user_cards)  # Deal user cards, adds to user list
        deal_cards(dealer_cards)    # Deal dealer cards, add to dealer list

    while continue_game:    # Loops game

        user_score = get_score(user_cards)  # Get updated user score
        dealer_score = get_score(dealer_cards)  # Get updated dealer score

        clear() # Clear console
        print(art.logo) # Print logo

        print(f"\nYour cards: {user_cards}, current score: {user_score}")   # Prints cards and score for user
        print(f"Computers first card: {dealer_cards[0]}")   # Prints first card in dealer hand

        # Checks for Blackjack or user score is over 21
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            continue_game = False   # End game
        else:
            # Check with user if they want another card
            player_hit = input("\nType Y if you would like another card, type N if you wish to pass: ").lower()

            if player_hit == "n":   # If no
                continue_game = False   # End game
            if player_hit == "y":   # If yes
                continue_game = True    # Continue game
                deal_cards(user_cards)  # Deal another card to user

    while get_score(dealer_cards) < 17: # While dealer score is less than 17
        deal_cards(dealer_cards)    # Deal another card for dealer

    clear() # Clear console
    print(art.logo) # Print logo
    winner = compare(user_cards, dealer_cards)  # Compares the final scores and winner
    print(f"\nYour final hand: {user_cards}, final score: {get_score(user_cards)}")    # Print final cards and user score
    print(f"Dealer final hand: {dealer_cards}, final score: {get_score(dealer_cards)}")    # Print final cards and dealer score

    print(f"\n{winner}")    # Output the winner message
    
    start_game = input("\nDo you want to play another game of Blackjack? Y or N: ").lower() # Prompt if user wants to play again

    if start_game == "y":   # If yes
        clear() # Clear console
        print(art.logo) # Print logo
        blackjack(start_game)   # Restart game
    else:   # If no
        return  # End game

blackjack(start_game)   # Call initial game