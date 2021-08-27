# Day 11 Blackjack

## Overview

Day 11 started with building a capstone project using just a list of requirements, basic knowledge of how to play Blackjack, and an example output.

    Blackjack 1.0 - Initial build of the capstone project
    Blackjack 2.0 - Enhanced build of the capstone project

## Project: Blackjack Card Game

Using what we learned in previous lectures, the goal of this project was to use that knowledge alone to build a basic Blackjack game. This game would include using functions, parameters, returns, variables, loops, conditional operators, lists, and other built-in functions. The game would deal the user 2 cards, and the user can choose to accept more cards, or end the game. Once the game ends, the total scores would be added and a winner declared.

### Instructions

The instructions provided were hints to help the user along the way if they wanted to use them, or test their skills without them. For `Blackjack 1.0`, I chose to use my prior experience and knowledge and the inforamation provided for how the game is played. For `Blackjack 2.0`, I modified the original build to clean it up and enhance it based on the hints provided below.

#### Requirements

1. The deck is unlimited in size.
2. There are no jokers.
3. The Jack/Queen/King all count as 10.
4. The the Ace can count as 11 or 1.
5. Use the following list as the deck of cards:
   1. cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
6. The cards in the list have equal probability of being drawn.
7. Cards are not removed from the deck as they are drawn.
8. The computer is the dealer.

#### Hints

    Difficulty Normal: Use all Hints below to complete the project.
    Difficulty Hard: Use only Hints 1, 2, 3 to complete the project.
    Difficulty Extra Hard: Only use Hints 1 & 2 to complete the project.
    Difficulty Expert: Only use Hint 1 to complete the project.

1. Check out these Blackjack demo's to familiarize with gameplay
   1. Go to this website and try out the Blackjack game: [Blackjack Demo](https://games.washingtonpost.com/games/blackjack/)
   2. Then try out the completed Blackjack project here: [Course Blackjack Demo](http://blackjack-final.appbrewery.repl.run)

2. Read this breakdown of program requirements: [Program Requirements](http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF)

3. Download and read this flow chart: [Blackjack Flowchart - Appbrewery](https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt)

4. Create a `deal_card()` function that uses the List below to *return* a random card from the list

    ```python
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ```

5. Deal the user and computer 2 cards each using `deal_card()` and `append()`

    ```python
    user_cards = []
    computer_cards = []
    ```

6. Create a function called `calculate_score()` that takes a List of cards as input and returns the score

        Look up the sum() function to help you do this.

7. Inside `calculate_score()` check for a blackjack, a hand with only 2 cards
   1. This is determined when there is an Ace (11) and a Jack, Queen or King(10)
   2. The cards will total 21
   3. Return 0 instead of the actual score, 0 will represent a blackjack in our game

8. Inside `calculate_score()` check for an Ace (11)
   1. If the score is already over 21, remove the 11 and replace it with a 1
   2. You might need to look up `append()` and `remove()`.

9. Call `calculate_score()`
   1. If the computer or the user has a blackjack (0)
   2. or if the user's score is over 21, then the game ends

10. If the game has not ended, ask the user if they want to draw another card
    1. If yes, then use the `deal_card()` function to add another card to the user_cards List
    2. If no, then the game ends

11. The score will need to be
    1. Rechecked with every new card drawn
    2. The checks in Hint 9 need to be repeated until the game ends

12. Once the user is done, it's time to let the computer play
    1. The computer should keep drawing cards as long as it has a score less than 17

13. Create a function called `compare()` and pass in the `user_score` and `computer_score`
    1. If the computer and user both have the same score, then it's a draw
    2. If the computer has a blackjack (0), then the user loses
    3. If the user has a blackjack (0), then the user wins
    4. If the user_score is over 21, then the user loses
    5. If the computer_score is over 21, then the computer loses
    6. If none of the above, then the player with the highest score wins.

14. Ask the user if they want to restart the game
    1. If they answer yes
       1. Clear the console and start a new game of blackjack
    2. If they answer no
       1. End the game

### Game Demo

[Replit Demo - Blackjack 1.0](https://replit.com/@EoghyUnscripted/Blackjack-10)
[Replit Demo - Blackjack 2.0](https://replit.com/@EoghyUnscripted/Blackjack-20)
