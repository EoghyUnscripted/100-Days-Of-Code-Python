"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 9
EXERCISE: 9-2 Travel Log
LEVEL: Beginner

"""

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country_name, visit_count, cities_visited):
    # Get parameters and append to travel log list as new nested dictionary
    travel_log.append({"country":country_name, "visits":visit_count, "cities":cities_visited})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])    # Call function with parameters
print(travel_log)