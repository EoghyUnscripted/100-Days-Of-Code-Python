"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 34
PROJECT: Quiz Game GUI
LEVEL: Advanced

"""

from tkinter import *
from Modules import quiz_brain


class QuizGameUI:
    
    
    def __init__(self, brain: quiz_brain.QuizBrain):
        
        self.THEME_COLOR = "#375362"     # GUI color variable
        self.quiz = brain   # Set quiz brain object
        
        # Window Setup
        self.window = Tk()  # Create GUI object
        self.window.title("Quizzler")   # Set title
        self.window.config(padx=20, pady=20, bg=self.THEME_COLOR)     # Set padding and background color
        
        # Label
        self.score_label = Label(text="Score: 0", fg="white", bg=self.THEME_COLOR)     # Set text, foreground, and background color
        self.score_label.grid(row=0, column=1)      # Position on grid
        
        self.canvas = Canvas(width=300, height=250, bg="white")     # Set canvas dimensions and background color
        self.canvas_text = self.canvas.create_text(150, 125, text="Question Text", width=200,
                                                     fill=self.THEME_COLOR, font=("Arial", 20, "italic"))  # Question text config
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)    # Position on grid
        
        # Buttons
        true_img = PhotoImage(file="Level 3 - Advanced/Day 34 - API GUI Quiz App/Images/true.png")  # Image file
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_button_press)    # Create true button
        self.true_button.grid(row=2, column=0)      # Position on grid
        
        false_img = PhotoImage(file="Level 3 - Advanced/Day 34 - API GUI Quiz App/Images/false.png")  # Image file
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_button_press)  # Create false button
        self.false_button.grid(row=2, column=1)     # Position on grid
        
        self.answer_key = self.get_next_question()    # Initiate ui with the first question
        
        self.window.mainloop()  # Keep window open


    def get_next_question(self):
        """ Function used to get next question. """
        
        # Reset canvas for each new question
        self.canvas.config(bg="white")   # Set backgroung color to white
        self.canvas.itemconfig(self.canvas_text, fill=self.THEME_COLOR)     # Set canvas text to default
            
        # Check for more questions
        if self.quiz.still_has_questions():     # If more questions available
            
            question = self.quiz.next_question()    # Call to get next question data
            self.canvas.itemconfig(self.canvas_text, text=question[0])    # Update canvas text with new question
            
        else:   # End of questions
            
            self.true_button.config(state="disabled")   # Disable button
            self.false_button.config(state="disabled")  # Disable button
            self.quiz.final_score(self.canvas, self.canvas_text)   # Call function to update final score
    
    
    def true_button_press(self):
        """ Function used when True button is selected. """
        
        self.feedback(self.quiz.check_answer("True"))   # Call feedback function
    
    
    def false_button_press(self):
        """ Function used when False button is selected. """
        
        self.feedback(self.quiz.check_answer("False"))  # Call feedback function
       
    
    def feedback(self, is_right):
        """ Function used to change UI background to red or green based on right or wrong guess. """
        
        if is_right:    # If correct guess
            
            self.canvas.config(bg="green")      # Set canvas color to green
            self.canvas.itemconfig(self.canvas_text, fill="#FFFFFF")    # Set text fill to white
            self.score_label.config(text=f"Score: {self.quiz.score}")   # Update score label
            
        else:   # If wrong guess
            
            self.canvas.config(bg="red")        # Set canvas color to red
            self.canvas.itemconfig(self.canvas_text, fill="#FFFFFF")    # Set text fill to white
        
        self.window.after(1000, self.get_next_question)     # Call next question after 1000ms