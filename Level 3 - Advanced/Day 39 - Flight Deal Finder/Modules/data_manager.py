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

from decouple import config
import requests


class DataManager:
    
    def __init__(self):
        self.sheety_endpoint = config("SHEETY_FP_ENDPOINT")     # Set endpoint url
        self.sheety_api = config("SHEETY_FP_API_KEY")           # Set API key
        self.sheety_headers = {
            "Authorization": self.sheety_api
            }                                                   # Set header dict
        self.destination_data = {}                               # Set empty dict for incoming data
            

    def put_To_Sheety(self):
        """ Function used to update rows on Google Sheets. """

        # Update Google Sheet data with new IATA codes
        for city in self.desination_data:
            
            # Set JSON to pass to API to update on Google Sheets
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                    "lowestPrice": city["lowestPrice"]
                }
            }
            
            # Call Sheety API to update Google Sheets with new data
            r = requests.put(url=f"{self.sheety_endpoint}/{city['id']}", json=new_data, headers=self.sheety_headers)
    
    
    def get_From_Sheety(self):
        """ Function used to get data from Google Sheets through Sheety API. """
        
        r = requests.get(self.sheety_endpoint, headers=self.sheety_headers)      # Call Sheety API
        data = r.json()["prices"]                                                # Convert to JSON
        self.destination_data = data                                             # Get nested dictionary
        
        return self.destination_data