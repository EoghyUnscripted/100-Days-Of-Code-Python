"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 26
EXERCISE: 26-4 Dictionary Comprehension 1
LEVEL: Intermediate

"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Get words in sentence and convert to dictionary and count total letter count for each word
result = {word: len(word) for word in sentence.split()}

print(result)
