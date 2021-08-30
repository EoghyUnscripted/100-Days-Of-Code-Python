import requests


question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


def replace_text(sentence):
    """Function for finding HTML entities and converting them to regular text."""
    string_check = sentence.replace("&quot;", "'")  # Replace &quot; with "
    new_string = string_check.replace("&#039;", "'")    # Replace &#039; with '
    return new_string   # Output new string


def get_question_list():
    """Function for getting API questions and appending to existing question list."""

    # Pull API data with GET request
    response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean")
    question_list = response.json()     # Convert to JSON

    for x in question_list["results"]:  # Loop through the API questions
        formatted_question = replace_text(x["question"])    # Format the string to remove HTML entities
        # Add API questions and answers to question list
        question_data.append({"text": formatted_question, "answer": x["correct_answer"]})

    return question_data    # Returns the updated list
