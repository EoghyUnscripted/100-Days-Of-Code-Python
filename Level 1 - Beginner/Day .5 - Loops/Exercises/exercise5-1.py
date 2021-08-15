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

INSTRUCTIONS:

    You are going to write a program that calculates the average student height from a List of heights.
    The average height can be calculated by adding all the heights together and dividing by the total number of heights.
    The output should be rounded to the nearest number.

    You should not use the `sum()` or `len()` functions in your answer.
    You should try to replicate their functionality using what you have learnt about for loops.

    Use the code provided -- do not change the existing code!

    CODE:

    student_heights = input("Input a list of student heights ").split()

    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

    # WRITE YOUR CODE HERE

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
    
