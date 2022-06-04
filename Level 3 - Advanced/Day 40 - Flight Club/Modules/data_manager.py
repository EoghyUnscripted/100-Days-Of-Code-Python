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

from decouple import config
import requests


class DataManager:
    
    def __init__(self):
        self.sheety_fp_endpoint = config("SHEETY_FP_ENDPOINT")     # Set prices endpoint url
        self.sheety_fcu_endpoint = config("SHEETY_FCU_ENDPOINT")   # Set users endpoint url
        self.sheety_api = config("SHEETY_FP_API_KEY")              # Set API key
        self.sheety_headers = {
            "Authorization": self.sheety_api
            }                                                      # Set header dict
        self.destination_data = {}                                 # Set empty dict for destination data
        self.users_data = {}                                       # Set empty dict for users data    

    def update_Destinations(self, destination, type=""):
        """ Function used to update rows on Google Sheets. """
        
        if type == "IATA":
            
            print(f"Updating IATA code for {destination['city']}...")
            
            # Set JSON to pass to API to update on Google Sheets
            new_data = {
                "price": {
                    "iataCode": destination["iataCode"]
                }
            }
        
            # Call Sheety API to update Google Sheets with new data
            requests.put(url=f"{self.sheety_fp_endpoint}/{destination['id']}", json=new_data, headers=self.sheety_headers)

        else:
            
            print(f"Updating price details for {destination['city']}...")
            
            # Set JSON to pass to API to update on Google Sheets
            new_data = {
                "price": {
                    "lowestPrice": destination["lowestPrice"]
                }
            }
        
            # Call Sheety API to update Google Sheets with new data
            requests.put(url=f"{self.sheety_fp_endpoint}/{destination['id']}", json=new_data, headers=self.sheety_headers)


    def get_Destinations(self):
        """ Function used to get destination data from Google Sheets through Sheety API. """
        
        print("Getting list of destinations...")
        
        r = requests.get(self.sheety_fp_endpoint, headers=self.sheety_headers)      # Call Sheety API
        data = r.json()["prices"]                                                # Convert to JSON
        self.destination_data = data                                             # Get nested dictionary
        
        return self.destination_data
    
    
    def get_Users(self):
        """ Function used to get user data from Google Sheets through Sheety API. """
        
        print("Getting email list...")
        
        r = requests.get(self.sheety_fcu_endpoint, headers=self.sheety_headers)      # Call Sheety API
        data = r.json()["users"]                                                # Convert to JSON
        self.users_data = data                                             # Get nested dictionary
        
        return self.users_data