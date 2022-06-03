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


from Modules import flight_search as fs, data_manager as dm, notification_manager as nm

data_manager = dm.DataManager()                     # Create a DataManager object
sheet_data = data_manager.get_From_Sheety()         # Create a dictionary with current Google Sheets data 
flight_search = fs.FlightSearch()                   # Create FlightSearch object
notification_manager = nm.NotificationManager()     # Create a NotificationsManager object

# Find rows with missing IATA Code in the data and update with IATA code
if sheet_data[0]["iataCode"] == "":
    
    for row in sheet_data:
        
        # Update the Sheety data with destination IATA Codes
        row["iataCode"] = flight_search.get_Destination_Code(row["city"])
    
    data_manager.desination_data = sheet_data   # Update dictionary in DataManager object
    data_manager.put_To_Sheety()                # Update Google Sheet with new data
    
    
# Check for flights to each city in Google Sheets list and get lowest price
for destination in sheet_data:
    
    # Update the Sheety data with destination IATA Codes
    flight = flight_search.get_Flights(destination)
    
    # Check if destination has flight data and if price is lower than Google Sheets data
    if flight is not None and flight.price < destination["lowestPrice"]:
    
        destination["lowestPrice"] = flight.price       # Set lower price
        
        message=(f"Low price alert! Only ${flight.price} to fly from {flight.departure_city}-{flight.departure_airport} "
                 + f"to {flight.destination_city}-{flight.destination_airport}, "
                 + f"from {flight.depart_date} to {flight.return_date}.")
        
        notification_manager.send_SMS(message)
    
data_manager.desination_data = sheet_data   # Update dictionary in DataManager object
data_manager.put_To_Sheety()                # Update Google Sheet with new data
    
    
    
