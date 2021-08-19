"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 5
EXERCISE: 5-1 Average Height
LEVEL: Beginner

"""

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

heightSum = 0
count = 0

for h in student_heights:
    heightSum += h # Get sum of all heights
    count += 1 # Get count of all heights

avgHeight = round(int(heightSum/count)) # Get the average height
print(f"The average height is: {avgHeight}")
    
