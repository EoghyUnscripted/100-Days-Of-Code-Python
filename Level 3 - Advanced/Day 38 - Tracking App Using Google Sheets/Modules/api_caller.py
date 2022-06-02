"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 38
PROJECT: Exercise Tracker
LEVEL: Advanced

"""

import requests
from decouple import config
from datetime import datetime as dt


def post_To_Nutritionix(message):
    """ Function used to post exercises to Nutritionix API. """

    # Nutritionix Environment Variables

    endpoint = config("NUTRIX_ENDPOINT")      # Set endpoint url
    api_key = config("NUTRIX_API_KEY")        # Set API key
    app_id = config("NUTRIX_APP_ID")          # Set APP ID

    # Nutritionix API Parameters
    headers = {
        "x-app-id": app_id,     # Pass APP ID
        "x-app-key": api_key        # Pass API Key
    }

    # NOTE: API allows users to pass age, height (cm), weight (kg), and sex (male/female) as options for more accurate calculations

    data = {
        "query": message      # Pass user input string
    }

    r = requests.post(f"{endpoint}", json=data, headers=headers)    # Post to API

    exercise_data = r.json()    # Return the API response data as dictionary

    return exercise_data


def post_To_Sheety(results):
    """ Function used to prepare results and call to Sheety API to post new rows to Google Sheets. """

    # Sheety Environment Variables

    endpoint = config("SHEETY_ENDPOINT")      # Set endpoint url
    api_key = config("SHEETY_API_KEY")        # Set API key

    # Sheety API Parameters

    # Nutritionix API Parameters
    headers = {
        "Authorization": api_key
    }
    
    today = dt.now().strftime("%m/%d/%Y")    # Create date object for today
    time = dt.now().strftime("%X")           # Create time object for today

    # Loop through all workouts returned from Nutritionix
    for exercise in results["exercises"]:

        sheet_inputs = {
            "workout": {
                "date": today,      # Today's date formatted to M/D/YYYY
                "time": time,       # Today's time in 24H format
                "exercise": exercise["name"].title(),   # Exercise name, capitalized
                "duration": exercise["duration_min"],   # Exercise duration in minutes
                "calories": exercise["nf_calories"]     # Exercise calories burned
            }
        }
        
        # NOTE: Keep the lines below as part of the for loop to post each exercise
    
        r = requests.post(f"{endpoint}", json=sheet_inputs, headers=headers)    # Post to API
        print(r.text)   # Print response from Sheety (optional)