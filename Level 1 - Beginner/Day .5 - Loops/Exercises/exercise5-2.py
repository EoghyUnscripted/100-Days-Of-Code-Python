"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 5
EXERCISE: 5-2 Highest Score
LEVEL: Beginner

"""

student_scores = input("Input a list of student scores ").split() # Get list of student scores

for n in range(0, len(student_scores)): # Loop through scores
  student_scores[n] = int(student_scores[n])  # Conver scores to integers
print(student_scores) # Output scores
    
highestScore = 0  # Set blank variable for highest score

for s in student_scores:  # Loop through scores
    # Test each number to find largest
    if s > highestScore:
        # Update with next largest number
        highestScore = s

print(f"The highest score in the class is: {highestScore}") # Output the highest score
