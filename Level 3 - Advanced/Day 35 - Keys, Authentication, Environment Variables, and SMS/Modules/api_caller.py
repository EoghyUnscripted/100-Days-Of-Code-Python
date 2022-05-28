"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 35
PROJECT: Rain Alert
LEVEL: Advanced

"""

import requests
from twilio.rest import Client


def get_Weather(endpoint, lat, lon, key):
    """ Function used to call API with passed parameters and return weather data. """
    
    # Set API parameters
    parameters = {
        "lat": lat,     # Latitude
        "lon": lon,     # Longitude
        "exclude": "current,minutely,daily",    # Do not include...
        "appid": key    # API Key
    }
    
    r = requests.get(endpoint, params=parameters)   # Call API to return data
    r.raise_for_status()    # Raise status code if error

    weather_data = r.json()["hourly"][:12]      # Filter the next 12 hours
    
    for i in weather_data:      # Loop through hourly data
        
        if i["weather"][0]["id"] < 700:     # Check if it will rain
            
            return True    # If it will rain
        

def send_SMS(account_sid, auth_token, from_num, to_num, body_text):
    """ Function used to call API to send an SMS message alert. """
    
    client = Client(account_sid, auth_token)    # Initiate Twilio client

    message = client.messages \
                    .create(
                        body=body_text,     # Message text
                        from_=from_num,     # From Twilio numbert
                        to=to_num           # To verified phone number
                    )

    print(message.status)   # Print status message to console
