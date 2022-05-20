"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 28
PROJECT: Pomodoro Timer
LEVEL: Intermediate

"""

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CYCLE = 0
MARKS = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """ Function used to reset the timer and Pomodoro Cycle. """
    global CYCLE    # Access global variable
    CYCLE = 0   # Set cycle count to default

    window.after_cancel(timer)  # Stop timer countdown
    title.config(text="Timer", fg=GREEN)  # Reset title label to "Timer"
    canvas.itemconfig(timer_text, text="00:00")  # Reset canvas timer to 00:00
    cycle.config(text="")   # Reset check marks label to blank


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """ Function used to call countdown and set minutes based on Pomodoro Cycle. """
    global CYCLE    # Access global variable

    CYCLE += 1  # Increment cycle by 1
    print(CYCLE)    # Print cycle count to console

    if CYCLE > 8:  # On 9th loop
        print("RESET")  # Print reset message to console
        reset_timer()   # Call function to stop timer and reset values
    else:   # Loops 1-8

        if CYCLE % 8 == 0:  # If cycle is on 8th turn, take long break
            count_down(LONG_BREAK_MIN * 60)     # Call countdown function and pass 20 minute timer
            title.config(text="Break", fg=RED)  # Update title to Break
        elif CYCLE % 2 == 0:    # If cycle is even, take a short break
            count_down(SHORT_BREAK_MIN * 60)  # Call countdown function and pass 5 minute timer
            title.config(text="Break", fg=PINK)     # Update title to Break
        elif CYCLE % 2 != 0:    # If cycle is odd
            count_down(WORK_MIN * 60)   # Call countdown function and pass 25 minute timer
            title.config(text="Work", fg=GREEN)     # Update title to Work

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """ Function used to update countdown based on minutes in Pomodoro Cycle. """
    global MARKS    # Access global variable

    count_min = math.floor(count / 60)  # Get total minutes
    count_sec = count % 60  # Get remaining seconds

    if 10 > int(count_min) > 0:     # If single digit minute
        count_min = f"0{count_min}"     # Display with a 0 first
    elif int(count_min) == 0:   # If 0 minutes
        count_min = "00"    # Display 00

    if 10 > int(count_sec) > 0:     # If single digit second
        count_sec = f"0{count_sec}"     # Display with 0 first
    elif int(count_sec) == 0:   # If 0 seconds
        count_sec = "00"    # Display 00

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Update timer_text variable on GUI
    if count > 0:   # Set to loop until 0
        global timer    # Access global variable
        timer = window.after(1000, count_down, count - 1)   # Refresh window every 1000 ms and reduce counter by 1
    else:
        start_timer()   # Call next timer
        MARKS = ""  # Set global variable to blank
        if CYCLE % 2 == 0:  # For every break
            work_sessions = math.floor(CYCLE/2)     # Count work sessions completed
            for _ in range(work_sessions):
                MARKS += "✓"    # Add a check mark after each work session
            cycle.config(text=MARKS)    # Update cycle label

# ---------------------------- UI SETUP ------------------------------- #


# Window Settings
window = Tk()   # Create window object
window.title("Pomodoro Timer")  # Set window title
window.config(padx=100, pady=50, bg=YELLOW)     # Set window padding and background color

# Canvas Settings
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)     # Set canvas dimensions, and bg color
# Set image file to create image
tomato_img = PhotoImage(file="Level 2 - Intermediate/Day 28 - Tkinter, Dynamic Typing, Pomodoro GUI/Images/tomato.png")
canvas.create_image(100, 112, image=tomato_img)     # Create image for canvas
# Set timer text, position, font
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)    # Set grid position

# Labels

# Create title label, set text and font
title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)   # Set grid position

# Create cycle label, set text and font
cycle = Label(font=(FONT_NAME, 24, "normal"), fg=GREEN, bg=YELLOW)
cycle.grid(column=1, row=3)   # Set grid position

# Buttons

# Create start button, set text, command, onclick
start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)    # Set grid position

# Create reset button, set text, command, onclick
reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)    # Set grid position

window.mainloop()   # Keep window open
