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

student_heights = input("Input a list of student heights ").split() # Get list of heights

for n in range(0, len(student_heights)):    # Loop through heights
    student_heights[n] = int(student_heights[n])    # Convert to integers

heightSum = 0   # Set blank variable to hold sum of heights
count = 0   # Set blank variable to hold count of heights

for h in student_heights:   # Loop through heights
    heightSum += h # Get sum of all heights
    count += 1 # Get count of all heights

avgHeight = round(int(heightSum/count)) # Get the average height
print(f"The average height is: {avgHeight}")    # Output the average height
    
