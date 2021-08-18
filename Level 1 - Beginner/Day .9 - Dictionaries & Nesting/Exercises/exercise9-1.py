"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 9
EXERCISE: 9-1 Grading Program
LEVEL: Beginner

INSTRUCTIONS:

    You have access to a database of `student_scores` in the format of a dictionary.
    The **keys** in `student_scores` are the **names** of the students and the **values** are their exam **scores**.

    Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` 
    that should contain student **names** for **keys** and their **grades** for **values**.

    The final version of the `student_grades` dictionary will be checked.
    
    **DO NOT** modify the existing `student_scores` dictionary.
    **DO NOT** write any print statements.

    1. Create an empty dictionary called student_grades.
    2. Write your code to add the grades to student_grades.

    This is the scoring criteria:

        - Scores 91 - 100: Grade = "Outstanding"
        - Scores 81 - 90: Grade = "Exceeds Expectations"
        - Scores 71 - 80: Grade = "Acceptable"
        - Scores 70 or lower: Grade = "Fail"

    Use the code provided -- do not change the existing code!

    CODE:

        student_scores = {
            "Harry": 81,
            "Ron": 78,
            "Hermione": 99, 
            "Draco": 74,
            "Neville": 62,
        }

        # WRITE YOUR CODE HERE

        print(student_grades)

"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}

student_grades = {} # Create empty dictionary

for grade in student_scores:    # Loop through student scores dictionary

    score = student_scores[grade]

    # Check the student score values
    # Add their name and grade level to empty student grades dictionary
    if score > 90:
        student_grades[grade] = "Outstanding"
    elif score > 80:
        student_grades[grade] = "Exceeds Expectations"
    elif score > 70:
        student_grades[grade] = "Acceptable"
    elif score < 70:
        student_grades[grade] = "Fail"

print(student_grades)   # Prints the new dictionary values