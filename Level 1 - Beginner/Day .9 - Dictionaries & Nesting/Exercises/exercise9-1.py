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