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

import requests
from Modules import question_model


def replace_text(sentence):
    """Function for finding HTML entities and converting them to regular text."""
    
    # Replace HTML codes for double spaces, single, double, left and right side quotes
    formatted_string = sentence.replace("  ", " ").replace("&quot;", "\"").replace("&#039;", "'").replace("&lsquo;", "'").replace("&rsquo;", "'")
    
    return formatted_string   # Output formatted string


def get_question_list():
    """Function for getting API questions and appending to existing question list."""

    question_list = [] # Set blank list to load random questions
    
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")   # Pull API data with GET request
    question_data = response.json()     # Convert to JSON

    for x in question_data["results"]:  # Loop through the API questions
        
        formatted_question = replace_text(x["question"])    # Format the string to remove HTML entities
        # Add API questions and answers to question list
        question_list.append({"text": formatted_question, "answer": x["correct_answer"]})

    return question_list    # Returns the updated list


def question_bank():
    """ Function used to create the question bank list for gameplay. """
    
    question_bank = []  # Empty list for new question objects

    # Loop through question list
    for row in get_question_list():
        
        question_text = row["text"]     # Get questions
        question_answer = row["answer"]     # Get answers
        # Create new question object for each question in list
        new_question = question_model.Question(question_text, question_answer)
        question_bank.append(new_question)  # Append to question bank list
        
    return question_bank