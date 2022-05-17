"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 25
EXERCISE: 25-2 Working With CSV - Squirrel Census
LEVEL: Intermediate

"""

import pandas

# Get data from the provided csv file 
data = pandas.read_csv("Level 2 - Intermediate/Day 25 - CSV Data, Pandas Library/Exercises/Modules/2018_squirrel_census.csv")

# Get the Primary Fur Color column into a list
fur_colors = data['Primary Fur Color'].to_list()

# Get the count of Black Squirrels
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])

# Get the count of Gray Squirrels
gray_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])

# Get the count of Red Squirrels
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])

# Create dictionary to pass into dataframe
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# Pass into dataframe
df = pandas.DataFrame(data_dict)

# Output to csv file
df.to_csv("Level 2 - Intermediate/Day 25 - CSV Data, Pandas Library/Exercises/Output/squirrel_counts.csv")