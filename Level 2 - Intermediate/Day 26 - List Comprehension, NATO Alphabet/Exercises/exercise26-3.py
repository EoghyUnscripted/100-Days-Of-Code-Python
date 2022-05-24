"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 26
EXERCISE: 26-3 Data Overlap
LEVEL: Intermediate

"""

# Get file contents from file1.txt
with open("Modules/file1.txt") as file1:
    file1_list = file1.readlines()

# Get file contents from file2.txt
with open("Modules/file2.txt") as file2:
    file2_list = file2.readlines()

# Create a new list with matching set between both files
result = [int(overlap) for overlap in file1_list if overlap in file2_list]

print(result)
