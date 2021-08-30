"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 17
PROJECT: The Quiz Game
LEVEL: Intermediate

"""

from Modules import data, question_model, quiz_brain

question_bank = []  # Empty list for new question objects

# Loop through question list
for row in data.get_question_list():
    question_text = row["text"]     # Get questions
    question_answer = row["answer"]     # Get answers
    # Create new question object for each question in list
    new_question = question_model.Question(question_text, question_answer)
    question_bank.append(new_question)  # Append to question bank list

quiz = quiz_brain.QuizBrain(question_bank)  # Create new quiz object

while quiz.still_has_questions():   # Loop through questions
    quiz.next_question()    # Get next question

final_score = quiz.score    # Get final score
final_percent = (quiz.score / len(quiz.question_list))*100  # Get final score percent
final_percent = int(final_percent)  # Convert percent to integer

# Output the final results of the quiz
print(f"You've completed the quiz.\n"
      f"Your final score is: {final_score}/{len(quiz.question_list)} or {final_percent}%.")
