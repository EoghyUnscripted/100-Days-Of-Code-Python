"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 19
PROJECT: Turtle Race
LEVEL: Intermediate

"""

import turtle as t
import random

t.setup(width=500, height=400)  # Set screen size
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]   # Set color options


def check_bets(turtle, bet):
    """Function used to compare winning turtle to user bet."""
    if turtle.pencolor() == bet.capitalize():   # If match
        print(f"You win! {bet} has won the race!")  # Print winning message
    else:   # If no match
        print(f"You lose. {turtle.pencolor()} has won the race!")   # Print losing message


def draw_finish_line():
    """Function used to draw a visible finish line."""
    race_line = t.Turtle()  # Create new turtle
    race_line.hideturtle()  # Hide turtle object from view
    race_line.penup()   # Pen up to prevent drawing
    race_line.goto(210, -200)   # Move turtle object to start of line
    race_line.setheading(90)    # Turn the turtle object to the left
    race_line.pendown()     # Pen down to draw line
    race_line.pencolor("gray")  # Set color of pen
    race_line.pensize(10)   # Set thickness of pen
    race_line.forward(400)  # Draw line to top of screen


def draw_winner_color(turtle_color):
    """Function used to display winning turtle color as text on screen."""
    winner_draw = t.Turtle()    # Create new turtle
    winner_draw.hideturtle()    # Hide turtle object from view
    winner_draw.penup()     # Pen up to prevent drawing
    winner_draw.goto(-200, -30)     # Move turtle object to the left of screen
    winner_draw.color(turtle_color)     # Set pen color to winning turtle object color
    winner_draw.pensize(10)     # Set thickness of pen
    # Set string and font details for the turtle object to display
    winner_draw.write(f"{turtle_color}!", font=("Arial", 60, "normal"))


def start_race(user_bet):
    """Function used to start the race with the turtle objects."""
    y_positions = [-150, -100, -50, 0, 50, 100, 150]    # Set starting line turtle object positions
    turtle_register = []    # Set empty list to store new turtle objects

    print(f"Your bet is: {user_bet}.")  # Display user's bet color

    draw_finish_line()  # Call function to draw finish line

    print("The race is starting!")  # Race starting message

    for turtle_index in range(0, 7):    # Loop through 1-7 to create turtle objects
        new_turtle = t.Turtle(shape="turtle")   # Create new turtle object with shape of turtle
        new_turtle.color(colors[turtle_index])  # Get color from indexes 0-6 for color choices
        new_turtle.penup()  # Pen up to prevent drawing
        new_turtle.goto(x=-230, y=y_positions[turtle_index])    # Move new turtle object to next y-position in list
        turtle_register.append(new_turtle)  # Add new turtle object to turtle list

    winner = False  # Boolean for While loop

    while not winner:   # While no winners

        for turtles in turtle_register:     # Loop through each turtle object in turtle list
            turtles.forward(random.randint(1, 31))      # Randomly move turtle object forward 1-30 paces

            if turtles.xcor() >= 210:   # If turtle is at or beyond finish line
                winner = True   # Set winner is True to stop while loop
                turtle_winner = turtles     # Get winning turtle object
                break   # Break the for loop to stop other turtle objects from moving forward

    check_bets(turtle_winner, user_bet)     # Call function to compare winning turtle object to user's bet
    draw_winner_color(turtle_winner.pencolor())     # Draw the color of the winning turtle object to the screen


def start_game():
    """Function used to start game and get user's bet."""
    validate = False    # Boolean for While loop

    while not validate:     # While input not validated
        # Get user's color bet
        user_bet = t.textinput("Place Your Bet!",
                               "Which turtle will win (Red, Orange, Yellow, Green, Blue, Indigo, Violet)?")

        if user_bet.capitalize() in colors:     # If color is an option from colors list
            validate = True     # Set boolean to True to stop while loop
            user_bet = user_bet.capitalize()    # Set users bet with a capital first letter
            break   # Break the while loop
        else:   # If color is not an option from colors list
            print(f"{user_bet} is not an option.\n"
                  "Try: Red, Orange, Yellow, Green, Blue, Indigo, or Violet.")  # Display error message to user

    start_race(user_bet=user_bet)   # Call function to start race with user's bet


start_game()    # Call the game to start
t.exitonclick()    # Keeps screen open until clicked
