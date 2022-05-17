"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 25
EXERCISE: 25-1 Working With CSV - Weather Data
LEVEL: Intermediate

"""

import pandas

# Get data from the provided csv file 
data = pandas.read_csv("Level 2 - Intermediate/Day 25 - CSV Data, Pandas Library/Exercises/Modules/weather_data.csv")

# Get the temperatures into a list
temps_list = data['temp'].to_list()
print("Temperatures: " + str(temps_list))

# Get the average temperature
avg_temp = data['temp'].mean()
print("Average Temp: " + str(avg_temp))

# Get the highest temperature
max_temp = data['temp'].max()
print("Max Temp: " + str(max_temp))
