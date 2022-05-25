"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 33
PROJECT: ISS Tracker
LEVEL: Advanced

"""

import requests
from datetime import datetime as dt
from pytz import UTC


def where_is_ISS():
    """ Function used to call API to return the current position of the ISS in longitude and latitude. """

    r = requests.get(url="http://api.open-notify.org/iss-now.json")     # API request
    r.raise_for_status()    # HTTP response code handling != 200

    position = r.json()['iss_position']     # Get JSON data for ISS position

    coordinates = (float(position['longitude']), float(position['latitude']))     # Set longitude and latitude as tuple
    
    return coordinates


def is_it_night(longitude, latitude):
    """ Function used to call API to return sunrise and sunset time for current longitude and latitude to check if it is dark out. """

    parameters = {
            'lat': latitude,     # Latitude
            'lng': longitude,     # Longitude
            'formatted': 0  # 24H
        }

    r = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)      # API request, pass current latitude and longitude
    r.raise_for_status()    # # HTTP response code handling != 200

    data = r.json()['results']  # Get JSON data for sunrise and sunset time

    format  = "%Y-%m-%d %H:%M:%S"   # Set datetime format
    now = dt.now(tz=UTC)    # Get local time in UTC
        
    local_date = (int(dt.now().month), int(dt.now().day))   # Get local month and day in a tuple
    time = str(dt.strptime(str(now)[:19], format)).strip(" ").strip(":")[11:19]   # Get the local time in UTC
    rise = str(dt.strptime(data['sunrise'].replace("T", " ")[:19], format)).strip(" ")[11:19]   # Get the time for sunrice in UTC
    set = str(dt.strptime(data['sunset'].replace("T", " ")[:19], format)).strip("")[11:19]      # Get the time for sunset in UTC

    # Check local date for DST
    if (5, 13) < local_date < (11, 6):
        
        time = time.replace(time[1], str(int(time[1]) - 1))     # Convert to DST time

    # Check if possible to see the ISS in the sky if nearby
    if rise[:2] > time[:2] > set[:2]:
        return True     # Night time
    else:
        return False    # Day time