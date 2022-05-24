"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 31
PROJECT: Flash Card App
LEVEL: Intermediate

"""

from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}     # Set blank list to store words to learn
new_card = {}   # Set blank dictionary to store card details

# ---------------------------- Flash Cards ------------------------------- #

def new_word():
    """ Function used to get a new word from the external csv file. """
    
    global new_card, timer, words_to_learn
    
    window.after_cancel(timer)  # Stop timer
    
    try: # Try to open words_to_learn.csv
        
        # Get data from csv file
        data = pandas.read_csv("Level 2 - Intermediate/Day 31 - Flash Card App/Output/words_to_learn.csv")
    
    except FileNotFoundError:   # If does not exist
        
        # Get data from original csv file
        data = pandas.read_csv("Level 2 - Intermediate/Day 31 - Flash Card App/Input/translations.csv")
    
    finally:    # Then run the rest of the code
        
        words_to_learn = data.to_dict(orient='records')   # Convert to dictionary
        new_card = choice(words_to_learn) # Get a random word    
        
        flash_card.itemconfig(card_title, text="Portuguese", fill="#000000")    # Set title text
        flash_card.itemconfig(card_word, text=new_card["portuguese"], fill="#000000")    # Set word text
        flash_card.itemconfig(card_background, image=card_front_img)     # Change the background image
        
        timer = window.after(3000, func=flip_card)  # Reset timer

def flip_card():
    """ Function used to flip the card. """
    
    flash_card.itemconfig(card_title, text="English", fill="#FFFFFF") # Set title text
    flash_card.itemconfig(card_word, text=new_card["english"], fill="#FFFFFF")    # Set word text
    flash_card.itemconfig(card_background, image=card_back_img)     # Change the background image
    
def learned_words():
    """ Function used to remove learned words from flash card list. """
    
    words_to_learn.remove(new_card) # Remove translation from list
    data = pandas.DataFrame(words_to_learn)     # Convert dictionary to dataframe
    data.to_csv("Level 2 - Intermediate/Day 31 - Flash Card App/Output/words_to_learn.csv", index=False)    # Save to file
    
    new_word()  # Call a new card

# ---------------------------- UI Setup ------------------------------- #

# Window Settings
window = Tk()   # Create window object
window.title("Flash Cards")  # Set window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)     # Set window padding and background color
timer = window.after(3000, func=flip_card)  # Set timer for card flip

# ---------------------------- Canvas Settings ------------------------------- #

# Flash Card

flash_card = Canvas(width=800, height=526)     # Set canvas dimensions
flash_card.config(highlightthickness=0, bg=BACKGROUND_COLOR)  # Set configurations

card_front_img = PhotoImage(file="Level 2 - Intermediate/Day 31 - Flash Card App/Images/card_front.png")    # Image file
card_back_img = PhotoImage(file="Level 2 - Intermediate/Day 31 - Flash Card App/Images/card_back.png")    # Image file
card_background = flash_card.create_image(400, 263, image=card_front_img)     # Create image for canvas

card_title = flash_card.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="#000000")  # Create title text
card_word = flash_card.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="#000000")   # Create word text

flash_card.grid(row=0, column=0, columnspan=2)    # Set grid position

# Buttons

wrong_img = PhotoImage(file="Level 2 - Intermediate/Day 31 - Flash Card App/Images/wrong.png")    # Image file
wrong_button = Button(image=wrong_img, command=new_word)  # Create wrong button image for canvas
wrong_button.grid(row=1, column=0)  # Set grid position

right_img = PhotoImage(file="Level 2 - Intermediate/Day 31 - Flash Card App/Images/right.png")    # Image file
right_button = Button(image=right_img, command=learned_words)  # Create right button image for canvas
right_button.grid(row=1, column=1)  # Set grid position

new_word()  # Call new card

window.mainloop()   # Keep window open