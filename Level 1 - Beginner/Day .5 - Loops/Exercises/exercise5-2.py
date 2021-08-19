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

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
    
highestScore = 0

for s in student_scores:
    # Test each number to find largest
    if s > highestScore:
        # Update with next largest number
        highestScore = s

print(f"The highest score in the class is: {highestScore}")
