"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 29
PROJECT: Password Manager
LEVEL: Intermediate

"""

from tkinter import *
from tkinter import messagebox
import pyperclip
from Modules import generator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    """ Function to generate random password, write to password input field, copy to clipboard. """
    
    password = generator.generate_password()     # Get randomly generated password from function
    pyperclip.copy(password)    # Copy password to clipboard
    password_input.insert(0, password)  # Insert password into text entry field
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_UI():
    """ Function used to clear the UI fields. """
    
    website_input.delete(0, END)    # Clear website entry box
    password_input.delete(0, END)  # Clear password entry box
    website_input.focus()   # Set focus to website entry box

def save_credentials():
    """ Function used to save the website, username, and password to a file. """
    
    website = website_input.get()   # Get website name
    username = email_username_input.get()   # Get username
    password = password_input.get()     # Get password
    
    # Validate text has been entered into entry boxes
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        
        # Alert user of missing fields
        messagebox.showwarning(title="Oops!", message="Please make sure all fields are filled.")
        
    else:
        
        # Confirm with user if credentials are correct
        is_ok = messagebox.askokcancel(title=website, message=f"These are your new credentials: \n"
                                                    + f"Username: {username} Password: {password}\n"
                                                    + f"Okay to save?")
        
        # If True, save to file
        if is_ok:
            
            # Open file for credentials
            with open("Level 2 - Intermediate/Day 29 - Tkinter Password Manager GUI/Output/password_file.txt", mode="a") as data_file:
                
                data_file.write(f"{website} | {username} | {password}\n")   # Append new credentials
            
            clear_UI() # Call to clear UI

# ---------------------------- UI SETUP ------------------------------- #

# Window Settings
window = Tk()   # Create window object
window.title("Password Manager")  # Set window title
window.config(padx=20, pady=20)     # Set window padding and background color

# Canvas Settings
canvas = Canvas(width=200, height=200, highlightthickness=0)     # Set canvas dimensions, and bg color
# Set image file to create image
logo_img = PhotoImage(file="Level 2 - Intermediate/Day 29 - Tkinter Password Manager GUI/Images/logo.png")
canvas.create_image(100, 100, image=logo_img)     # Create image for canvas
canvas.grid(row=0, column=1)    # Set grid position

# Labels

# Create website label, set text and font
website = Label(text="Website:")
website.grid(row=1, column=0)   # Set grid position

# Create email/username label, set text and font
email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)   # Set grid position

# Create password label, set text and font
password = Label(text="Password:")
password.grid(row=3, column=0)   # Set grid position

# Text Entry Boxes

website_input = Entry(width=35)    # Create input box, set width
website_input.grid(row=1, column=1, columnspan=2)    # Set grid position
website_input.focus()   # Sets cursor to website text entry box

email_username_input = Entry(width=35)    # Create input box, set width
email_username_input.grid(row=2, column=1, columnspan=2)    # Set grid position
email_username_input.insert(0, "example@email.com")    # Set default placeholder

password_input = Entry(width=20)    # Create input box, set width
password_input.grid(row=3, column=1)    # Set grid position

# Buttons

# Create generate button, set text, command, onclick
random_password = Button(text="Generate", width=10, command=generate)
random_password.grid(row=3, column=2)    # Set grid position

# Create add password button, set text, command, onclick
add_pass = Button(text="Add", width=33, command=save_credentials)
add_pass.grid(row=4, column=1, columnspan=2)    # Set grid position

window.mainloop()   # Keep window open