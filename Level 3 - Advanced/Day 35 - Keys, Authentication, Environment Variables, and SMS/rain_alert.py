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

import os
from Modules import api_caller

# Weathr API Variable Setup

api_key = os.environ.get("OWM_API_KEY")    # Set your API key
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"    # Endpoint
lat = 0     # Set your latitude
lon = 0     # Set your longitude
will_it_rain = api_caller.get_Weather(weather_endpoint, lat, lon, api_key)      # Check for rain

# Twilio API Variable Setup

account_sid = os.environ.get("T_ACC_SID")    # Enter your Twilio Account SID
auth_token = os.environ.get("T_AUTH_TOKEN")     # Enter your Twilio Auth Token
from_num = "+10000000000"      # Enter your Twilio phone number w/ country code
to_num = "+10000000000"        # Enter a Twilio verified phone number w/ country code
body_text = "Bring an umbrella!"      # Enter the body text you want to send


if will_it_rain:    # If it will rain today
    
    # Call function to send SMS alert, pass Twilio variables
    api_caller.send_SMS(account_sid, auth_token, from_num, to_num, body_text)