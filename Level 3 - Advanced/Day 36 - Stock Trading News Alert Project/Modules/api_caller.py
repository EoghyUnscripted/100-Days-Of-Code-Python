"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 36
PROJECT: Stock Alerts
LEVEL: Advanced

"""

import requests
from twilio.rest import Client


def check_stocks(endpoint, key, stock):
    """ Function used to get closing stock changes from prior two days.
        Passes endpoint url, API key, and stock abbreviation. """
    
    # Stock API Parameters
    parameters = {
        "function": "TIME_SERIES_DAILY",    # Get recent daily stock results
        "outputsize": "COMPACT",        # Shorten results to last 100 days
        "symbol": stock,        # Company stock abbreviation
        "apikey": key       # Your API key
    }
    
    up_down = None      # None variable for up or down emoji
    
    r = requests.get(endpoint, params=parameters)   # Call API to return data
    r.raise_for_status()    # Raise status code if error

    response_json = r.json()["Time Series (Daily)"]     # Filter the nested data
    daily_stock = [value for (key, value) in response_json.items()]     # Create a python list of the values for each day

    # Get difference between last two days
    difference = float(daily_stock[0]["4. close"]) - float(daily_stock[1]["4. close"])     # Get closing price difference
    percent = round((difference / float(daily_stock[0]["4. close"]) * 100))    # Get the difference in percent, rounded
    
    # Check if stock increased or decreased and set up or down arrow
    
    if difference > 0:  # If increase in stock price
        
        up_down = "🔺"
        
    else:   # If decrease in stock price
        
        up_down = "🔻"
        
    # Check if percentage of price change is significant

    if abs(percent) > 5:     # If there is a change greater than 5%
            
        return (True, up_down, percent)
    
    return False
    
    
def check_news(endpoint, key, stock, emoji, difference):
    """ Function used to get stock news articles. 
        Passes endpoint url, API key, stock abbreviation name, emoji icon, and percent change. """
    
    # News API Parameters
    parameters = {
        "apiKey": key,          # Your API key
        "qInTitle": stock,      # Company stock abbreviation 
    }
    
    r = requests.get(endpoint, params=parameters)   # Call API to return data
    r.raise_for_status()    # Raise status code if error
    
    articles = r.json()["articles"][:3]     # Filter first 3 articles
    
    # Format output for sms to pass through return variable
    output_message = [f"{stock}: {emoji} {difference}%\n{article['title']}\n"
                      + f"\n{article['url']}" 
                      for article in articles]
    
    return output_message


def send_SMS(account_sid, auth_token, from_num, to_num, body_text):
    """ Function used to call API to send an SMS message alert. 
        Passes Account SID, Auth Token, Twilio Number, Verified Phone Number, and body content. """
    
    client = Client(account_sid, auth_token)    # Initiate Twilio client

    message = client.messages \
                    .create(
                        body=body_text,     # Message text
                        from_=from_num,     # From Twilio numbert
                        to=to_num           # To verified phone number
                    )

    print(message.status)   # Print status message to console