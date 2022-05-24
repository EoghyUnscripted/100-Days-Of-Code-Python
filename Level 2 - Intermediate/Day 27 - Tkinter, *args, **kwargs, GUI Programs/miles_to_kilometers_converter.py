"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 27
PROJECT: Miles to Kilometers Converter
LEVEL: Intermediate

"""

from tkinter import *


def button_click():
    """ Function used to execute command on button click. """
    user_says = float(user_input.get())     # Get user input as integer
    km = round(user_says * 1.61)    # Convert miles to km and round
    label_2.config(text=f"{km}")    # Reset the label with new text


# Window Settings
window = Tk()   # Initialize a new GUI window
window.title("Miles to Kilometers Converter")   # Set a title
window.config(padx=20, pady=20)     # Set the window padding

# Labels
label_1 = Label(text="is equal to", font=("Arial", 12, "bold"))     # Create label, set text and font
label_1.grid(column=0, row=2)   # Set grid position

label_2 = Label(text="0", font=("Arial", 12))   # Create label, set text and font
label_2.grid(column=1, row=2)   # Set grid position

label_3 = Label(text="Miles", font=("Arial", 12))   # Create label, set text and font
label_3.grid(column=2, row=1)   # Set grid position

label_4 = Label(text="Km", font=("Arial", 12))  # Create label, set text and font
label_4.grid(column=2, row=2)   # Set grid position

# Buttons
button = Button(text="Calculate", command=button_click)     # Create button, set text and command onclick
button.grid(column=1, row=3)    # Set grid position

# Entry
user_input = Entry(width=10)    # Create input box, set width
user_input.grid(column=1, row=1)    # Set grid position

window.mainloop()   # Keep window open
