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

class QuizBrain:

    def __init__(self, question_list):
        
        self.question_id = 0    # Set default ID to 0
        self.question_list = question_list      # Get new question bank
        self.score = 0      # Set default score to 0
        self.current_question = []  # Set current question and answer key


    def still_has_questions(self):
        """Function to check if there are more questions in the list."""
        
        return self.question_id < len(self.question_list)   # Returns True or False


    def next_question(self):
        """Function to prompt next question and accept user guess if True or False."""
        
        # Track current question
        self.current_question = self.question_list[self.question_id]     # Get current question
        self.question_id += 1   # Set ID so questions start at 1 instead of 0
        
        # Get next question and answer strings as variables for return tuple
        next_question = f"Q.{self.question_id}: {self.current_question.text} (True/False): "    # Get next question string
        next_answer = self.current_question.answer      # Get answer string
        
        return (next_question, next_answer)


    def check_answer(self, guess):
        """Function to check if user guess is the correct answer."""
        
        if guess.lower() == self.current_question.answer.lower():     # If guess matches answer
            
            self.score += 1     # Add a point to the score
            
            return True
        
        else:   # If wrong
            
            return False
        
        
    def final_score(self, quiz, canvas):
        """ Function used to get the final score at the end of the quiz. """
        
        final_score = self.score    # Get final score
        final_percent = int((self.score / len(self.question_list))*100)  # Get final score percent
        
        output = (f"You've completed the quiz.\n\nYour final score is: "
                  f"{final_score}/{len(self.question_list)} or {final_percent}%.")      # Final score output string
        
        # Update canvas config and text based on final score
        
        quiz.itemconfig(canvas, text=output)    # Update canvas text with output message
        
        if final_percent > 60:     # If score is above 60%
                
            quiz.config(bg="green")  # Set canvas color to green
            quiz.itemconfig(canvas, fill="#FFFFFF")    # Set text fill to white
                
        else:   # If score below 60%
            
            quiz.config(bg="red")    # Set canvas color to red
            quiz.itemconfig(canvas, fill="#FFFFFF")    # Set text fill to white
