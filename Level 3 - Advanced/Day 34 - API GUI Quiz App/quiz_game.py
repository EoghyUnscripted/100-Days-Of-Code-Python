"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 34
PROJECT: Quiz Game
LEVEL: Advanced

"""

from Modules import ui, data, quiz_brain

# Initialize Quiz Game

question_bank = data.question_bank()    # Get trivia questions for gameplay
quiz = quiz_brain.QuizBrain(question_bank)  # Create new quiz object
quiz_ui = ui.QuizGameUI(quiz)   # Create new UI
