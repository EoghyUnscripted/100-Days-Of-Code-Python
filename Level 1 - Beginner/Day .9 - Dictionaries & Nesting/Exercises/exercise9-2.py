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

INSTRUCTIONS:

    You are going to write a program that adds to a `travel_log`. You can see a travel_log which is a **List** that contains 2 **Dictionaries**.

    Write a function that will work with the following line of code to add the entry for Russia to the `travel_log`:

        add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

    Use the code provided -- do not change the existing code!

    CODE:

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

        # WRITE YOUR CODE HERE

        add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
        print(travel_log)

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

def add_new_country(country, visits, places):
    travel_log.append({"country":country, "visits":visits, "places":places})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)