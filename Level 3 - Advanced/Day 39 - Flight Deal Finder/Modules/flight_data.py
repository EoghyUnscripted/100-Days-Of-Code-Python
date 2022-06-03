"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 39
PROJECT: Capstone Project Part 1 - Cheap Flight Finder
LEVEL: Advanced

"""


class FlightData:
    
    def __init__(self, departure_city, departure_airport, destination_city, destination_airport, depart_date, return_date, price):
        self.departure_city = departure_city                        # Departure city name
        self.departure_airport = departure_airport                  # Departure city IATA Code
        self.destination_city = destination_city                    # Destination city name
        self.destination_airport = destination_airport              # Destination city IATA Code
        self.depart_date = depart_date                              # Departure flight date
        self.return_date = return_date                              # Return flight date
        self.price = price                                          # Round trip price
