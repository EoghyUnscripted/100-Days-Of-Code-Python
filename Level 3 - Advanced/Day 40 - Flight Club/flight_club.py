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


import pyshorteners
from Modules import flight_search as fs, data_manager as dm, notification_manager as nm

data_manager = dm.DataManager()                     # Create a DataManager object
flight_search = fs.FlightSearch()                   # Create FlightSearch object
notification_manager = nm.NotificationManager()     # Create a NotificationsManager object

destination_data = data_manager.get_Destinations()    # Create a dictionary with current destinations data
user_data = data_manager.get_Users()                  # Create a dictionary with current users data

# Find rows with missing IATA Code in the data and update with IATA code
if destination_data[0]["iataCode"] == "":
    
    for row in destination_data:
        
        # Update the Sheety data with destination IATA Codes
        row["iataCode"] = flight_search.get_Destination_Code(row["city"])
    
        data_manager.desination_data = destination_data   # Update dictionary in DataManager object
        data_manager.update_Destinations(row, "IATA")     # Update Google Sheet with new data
    
    
# Check for flights to each city in Google Sheets list and get lowest price
for destination in destination_data:
    
    # Update the Sheety data with destination IATA Codes
    flight = flight_search.get_Flights(destination)
    
    # Check if destination has flight data and if price is lower than Google Sheets data
    if flight is not None and flight.price < destination["lowestPrice"]:
    
        destination["lowestPrice"] = flight.price           # Set lowest price
        
        tiny_url = pyshorteners.Shortener()                 # Initialize a url shortener object
        booking = tiny_url.tinyurl.short(flight.link)       # Shorten the url
            
        # Message to user about the flight deal, including link to book on Kiwi
        message= (f"Low price alert!\n\nOnly ${flight.price} to fly from {flight.departure_city}-{flight.departure_airport} "
                 + f"to {flight.destination_city}-{flight.destination_airport}, "
                 + f"from {flight.depart_date} to {flight.return_date}.\n\n"
                 + f"Click to book on Kiwi: {booking}")
        
        if flight.layovers > 0:     # If flight has a layover
            
            # Include message to user about layover and the city name
            message += f"\n\nThis flight has {flight.layovers} layover in {flight.via_city}."
    
        data_manager.desination_data = destination_data   # Update dictionary in DataManager object
        data_manager.update_Destinations(destination)     # Update Google Sheet with new data
        
        notification_manager.send_Email(user_data, message)    # Send email notification
