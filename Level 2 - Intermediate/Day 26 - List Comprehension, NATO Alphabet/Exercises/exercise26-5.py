"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 26
EXERCISE: 26-4 Dictionary Comprehension 2
LEVEL: Intermediate

"""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# Get each day and temperature and convert the temp to fahrenheit in a new dictionary
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

print(weather_f)
