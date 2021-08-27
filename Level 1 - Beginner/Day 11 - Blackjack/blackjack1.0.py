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

    if start_game == "n":   # If user does not want to play
        return  # Stops the program

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    # List of cards to deal
    user_cards = [] # Stores dealt cards for user
    dealer_cards = []   # Stores dealt cards for dealer

    def deal_cards():
        """Function to randomly select a card from the deck and returns the index."""
        get_card = random.randint(1,len(cards) - 1) # Get random index from cards list
        return get_card # Return index

    def compare_scores():
        """Function to calculate final scores at the end of the game and determine the winner"""
        scores = get_scores() # Calls function to get updated scores for each hand

        if scores["Dealer"] < 17:   # Checks id dealer hand has less than 17
            dealer_cards.append(cards[deal_cards()])    # Pulls another card
            scores = get_scores()   # Updates the score
            
        dealer_score = scores["Dealer"] # Get the dealer score and set to variable
        user_score = scores["User"] # Get the user score and set to variable

        # Loops during first deal of 2 cards if check_score() triggers false
        if len(user_cards) == 2:
            # Checks if Blackjack on first round 
            if 11 in user_cards and 10 in user_cards:   # Ace and Jack/Queen/King
                return "User with Blackjack"    # User wins automatically
        if len(dealer_cards) == 2:
            # Checks if Blackjack on first round
            if 11 in dealer_cards and 10 in dealer_cards:   # Ace and Jack/Queen/King
                return "Dealer with Blackjack"  # Dealer wins automatically

        # Determines if Ace is 11 or 1
        if 11 in user_cards and user_score > 21:    # If over 21, Ace is 1
            user_score -= 10    # Subtracts 10 from score
        elif 11 in dealer_cards and dealer_score > 21:  # If over 21, Ace is 1
            dealer_score -= 10  # Subracts 10 from score

        if user_score > 21 and dealer_score > 21:   # If both hands are over 21
            return "Neither"    # No winner

        if user_score > 21: # If user score is over 21
            return "Dealer" # Dealer wins
        elif dealer_score > 21: # If dealer score is over 21
            return "User"   # User wins
        elif user_score == dealer_score:    # If score is the same
            return "Draw"   # Tied
        elif user_score > dealer_score: # If user score is greater than dealers
            return "User"   # User wins
        elif dealer_score > user_score: # If dealer score is greater than users
            return "Dealer" # Dealer wins

    def check_hands():
        """Function used to check each players hand during game play for certain conditions and determines if game continues or ends."""
        user_score = sum(user_cards)    # Checks sum of user cards
        dealer_score = sum(dealer_cards)    # Checks sum of dealer cards
        
        if user_score > 21 and dealer_score > 21:   # If both hands are over 21
            return True # End game

        # Loops during first deal of 2 cards
        if len(user_cards) == 2:
            # Checks if Blackjack on first round
            if 11 in user_cards and 10 in user_cards:
                return True    # End game
        if len(dealer_cards) == 2:
            # Checks if Blackjack on first round
            if 11 in dealer_cards and 10 in dealer_cards:
                return True    # End game
        
        if user_score > 21: # If user score is over 21
            return True # End game
        elif dealer_score > 21: # If dealer score is over 21
            return True # End game
        else:   # If no condition is met
            return False    # Continue game

    def get_scores():
        """Function used to calculate current scores for user and dealer and sets to dictionary."""
        user_score = sum(user_cards)    # Get user score
        dealer_score = sum(dealer_cards)    # Get dealer score
        scores = {
            "User":user_score,  # Set user score
            "Dealer":dealer_score   # Set dealer score
        }
        return scores   # Return the dictionary

    for i in range(0,2):    # Deals first round of cards
        user_cards.append(cards[deal_cards()])  # Deal user cards, adds to user list
        dealer_cards.append(cards[deal_cards()])    # Deal dealer cards, add to dealer list

    hit_card = True # Sets conditional for looping game play

    while hit_card: # While true
        scores = get_scores()   # Get initial/updated scores
        print(f"\nYour cards: {user_cards}, current score: {scores['User']}")   # Prints cards and score for user
        print(f"Computers first card: {dealer_cards[0]}")   # Prints first card in dealer hand

        if check_hands():   # Checks if conditions are met to end game
            hit_card = False    # Stops loop if true
        else:   # If false, continue
            hit = input("\nType Y to get another card, N to pass: ").lower() # Check if user wants another card
            
            if hit == "n":  # If no
                hit_card = False    # Stop loop
                compare_scores()    # Get results of game
                scores = get_scores()   # Update the scores
            elif hit == "y":    # If yes
                clear() # Clear console
                print(art.logo) # Print logo
                user_cards.append(cards[deal_cards()])  # Get and add next card to users list
                dealer_cards.append(cards[deal_cards()])    # Get and add next card to dealers list
    
    clear() # Clear console
    print(art.logo) # Print logo
    print(f"\nYour final hand: {user_cards}, final score: {scores['User']}")    # Print final cards and user score
    print(f"Dealer final hand: {dealer_cards}, final score: {scores['Dealer']}")    # Print final cards and dealer score
    winner = compare_scores()   # Compare the hands one more time for updates
    print(f"\nThe winner is: {winner}!")    # Print the winner name
    start_game = input("\nDo you want to play another game of Blackjack? Y or N: ").lower() # Prompt if user wants to play again

    if start_game == "y":   # If yes
        clear() # Clear console
        print(art.logo) # Print logo
        blackjack(start_game)   # Restart game
    else:   # If no
        return  # End game

blackjack(start_game)   # Call initial game