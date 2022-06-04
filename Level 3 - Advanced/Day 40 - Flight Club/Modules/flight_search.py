"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 40
PROJECT: Capstone Project Part 2 - Flight Club
LEVEL: Advanced

"""

from Modules import flight_data as fd
from datetime import datetime as dt, timedelta
from decouple import config
import requests, os


class FlightSearch:
    
    
    def __init__(self):
        self.kiwi_endpoint = config("KIWI_ENDPOINT")     # Set endpoint url
        self.kiwi_api = config("KIWI_API_KEY")           # Set API key
        self.kiwi_headers = {
            "apikey": self.kiwi_api
            }                                                     # Pass header variables
        self.tomorrow = dt.now() + timedelta(days=1)              # Set start date for search
        self.six_months = dt.now() + timedelta(days=(6 *30))      # Set end date for search
        
        
    def get_Flights(self, destinations, layover=0):
        """ Function used to call Kiwi API to get flight data within passed parameters. """
        
        departure = "SEA"       # Default departure IATA code for SEATTLE, WA
        
        check_list = {
            "fly_from": departure,                              # Required departure IATA Code
            "fly_to": destinations["iataCode"],                 # Required destination IATA Code
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),    # Required
            "date_to": self.six_months.strftime("%d/%m/%Y"),    # Required
            "adults": 1,                                        # Optional: Narrows results
            "curr": "USD",                                      # Set to USD currency                   
            "nights_in_dst_from": 7,                            # Set 7 days minimum in destination
            "nights_in_dst_to": 28,                             # Set 28 days maximum in destination
            "flight_type": "round",                             # Set round trip
            "one_for_city": 1,                                  # Set for lowest price flight for city
            "max_stopovers": layover                            # Set no layovers by default
            }
        
        try:
            
            print(f"Checking direct flights to {destinations['city']}...")
            
            # Make API call to search for flights using passed parameter variable data
            r = requests.get(f"{self.kiwi_endpoint}/v2/search", params=check_list, headers=self.kiwi_headers)
            
            flight = r.json()["data"][0]    # Check for returned flight data
            
        except IndexError:
            
            print(f"There are no direct flights to {destinations['city']}.")
            
            # Update checklist to include 1 layover
            check_list["max_stopovers"] = 1
            
            try:
            
                print(f"Checking flights with 1 layover to {destinations['city']}...")
                
                # Make API call to search for flights with 1 layover using passed parameter variable data
                r = requests.get(f"{self.kiwi_endpoint}/v2/search", params=check_list, headers=self.kiwi_headers)
                
                flight = r.json()["data"][0]    # Check for returned flight data
                
            except IndexError:
                
                print(f"There are no flight deals to {destinations['city']}.")
                
                # If there are also no flights with 1 layover
                return None
            
            else:
            
                # Create flight data object to store returned data, including layover data
                flight_data = fd.FlightData(
                    departure_city = flight["route"][0]["cityFrom"],
                    departure_airport = flight["route"][0]["flyFrom"],
                    destination_city = flight["route"][1]["cityTo"],
                    destination_airport = flight["route"][1]["flyTo"],
                    depart_date = flight["route"][0]["local_departure"].split("T")[0],
                    return_date = flight["route"][1]["local_departure"].split("T")[0],
                    price = flight["price"],
                    link = flight["deep_link"],
                    layovers = 1,
                    via_city = flight["route"][0]["cityTo"]
                    
                )
                
                return flight_data        
        
        else:
        
            # Create flight data object to store returned data
            flight_data = fd.FlightData(
                departure_city = flight["route"][0]["cityFrom"],
                departure_airport = flight["route"][0]["flyFrom"],
                destination_city = flight["route"][0]["cityTo"],
                destination_airport = flight["route"][0]["flyTo"],
                depart_date = flight["route"][0]["local_departure"].split("T")[0],
                return_date = flight["route"][1]["local_departure"].split("T")[0],
                price = flight["price"],
                link = flight["deep_link"]
            )
        
        return flight_data
        
    
    def get_Destination_Code(self, city):
        """ Function used to get the IATA code for the destination city. """
        
        # Kiwi API parameters to query IATA Codes
        check_list = {
            "term": city,
            "location_types": "city"
            }
        
        # Call Kiwi API to get data for passed city name
        r = requests.get(url=f"{self.kiwi_endpoint}/locations/query", params=check_list, headers=self.kiwi_headers)
        code = r.json()["locations"][0]["code"]     # Locate the IATA code to return
        
        return code
        