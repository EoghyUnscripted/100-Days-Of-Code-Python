"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 9
PROJECT: Secret Auction
LEVEL: Beginner

"""

from Modules import art
import os

print(art.logo)
print('Welcome to the Secret Auction!')

more_bids = True    # Boolean to determine when to stop loop
bids = {}   # Empty dictionary to store new bids

def clear(): 
    os.system('clear') #on Linux System

def bid_checker():
    
    highest_bid = 0    # Empty variable to store highest bid amount
    highest_bidder = "" # Empty variable to store highest bid name

    for bidder in bids: # Loop through bids to find highest amount

        if bids[bidder] > highest_bid:  # If next bid is higher than the last highest
            highest_bid = bids[bidder]  # Update bid amount variable
            highest_bidder = bidder # Update bidder name variable

    print(f'\nThe winner is {highest_bidder} with the amount of ${highest_bid}!')

while more_bids:

    bidder_name = input('\nWhat is your name?: ')   # Get name
    bidder_amount = int(input('\nHow much would you like to bid?: $'))   # Get bid amount

    bids[bidder_name] = bidder_amount   # Add to new bids dictionary

    next_bidder = input('\nAre there any more bidders? (Y or N): ').upper() # Check if more bidders

    # If not, stops the loop
    if next_bidder == 'N':
        more_bids = False   # Sets to false
        clear() # Clear console Lunux
        bid_checker()   # Calls function to check bids
    else:
        clear() # Clear console Linux for next loop
