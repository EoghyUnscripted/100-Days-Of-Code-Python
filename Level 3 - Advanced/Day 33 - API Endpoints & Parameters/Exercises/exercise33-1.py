"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 33
EXERCISE: 33-1 Kanye Quotes API
LEVEL: Advanced

"""

from tkinter import *
import requests


def get_quote():
    """ Function used to get a new quote from Kanye.rest as JSON. """
    
    r = requests.get(url="https://api.kanye.rest/")     # Request API response
    quote = r.json()['quote']   # Decode JSON data to pull quote
    canvas.itemconfig(quote_text, text=quote)   # Update canvas text with new quote


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="#FFFFFF")

canvas = Canvas(width=300, height=414, highlightthickness=0, bg="#FFFFFF")
background_img = PhotoImage(file="Level 3 - Advanced/Day 33 - API Endpoints & Parameters/Exercises/Images/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Level 3 - Advanced/Day 33 - API Endpoints & Parameters/Exercises/Images/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bd=0)
kanye_button.grid(row=1, column=0)

window.mainloop()