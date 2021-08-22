# Day 9 Dictionaries & Nesting

## Overview

Day 9 starts with using dictionaries and lists and learning how to nest them. From there we move into building a Secret Auction appliction.

    Exercise 9.1 - Create a program that takes student grades from a dictionary and populates a new one with the converted grade levels
    Exercise 9.2 - Build a function that accepts a nested dictionary and adds it to an existing dictionary nested within a list

## Project: Secret Auction

Using what was learned from the exercises, the final project for Day 9 was to build a Secret Auction program. The program would allow bidders to enter their name and bid amount and hide the console data if there were more bids to be entered. The final output would get the highest bid and output the name and bid amount for the winner.

### Instructions

1. Import and print the logo from art.py when the program starts.

2. Get user input for:
    1. Name (key)
    2. Bid Amount (value)

3. Add name and bid amount to a dictionary as key and value

4. Ask if there are any other users who want to bid
    1. If `YES`:
       1. Clear the screen
       2. Loop again
    2. If `NO`:
       1. Find the highest bid in the dictionary
       2. Declare them the winner

### Flow Chart

![Alt Image](Images/secret_auction_flow_chart.png)
