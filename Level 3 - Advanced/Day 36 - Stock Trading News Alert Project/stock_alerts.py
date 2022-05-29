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

from decouple import config
from Modules import api_caller


# Stock API Variable Setup

stock_key = config("AV_API_KEY")    # Stock API key
stock_endpoint = config("AV_ENDPOINT")      # Stock endpoint address
stock_name = "MET"     # Enter the stock name to check

# News API Variable Setup

news_key = config("NEWS_API_KEY")   # News API key
news_endpoint = config("NEWS_ENDPOINT")     # News endpoint address

# Twilio API Variable Setup

account_sid = config("TWILIO_ACCT_SID")    # Enter your Twilio Account SID
auth_token = config("TWILIO_AUTH_TOKEN")     # Enter your Twilio Auth Token
from_num = config("TWILIO_PHONE")     # Enter your Twilio phone number w/ country code
to_num = config("TWILIO_VERIFIED_PHONE")        # Enter a Twilio verified phone number w/ country code

# NOTE: Twilio does not need an endpoint address with twilio-CLI installed

# Get stock check return tuple
stock_check = api_caller.check_stocks(stock_endpoint, stock_key, stock_name)

# Check if there is a significant change in stock prices in the last two days

try:

    if stock_check[0]:      # If returned True
        
        emoji, difference = stock_check[1], stock_check[2]      # Get passed variables for message formatting
        
        # Get 3 recent news articles relating to company
        messages = api_caller.check_news(news_endpoint, news_key, stock_name, emoji, difference)
        
        for message in messages:    # Call Twilio API for each article.
            
            api_caller.send_SMS(account_sid, auth_token, from_num, to_num, message)     # Send SMS message
            
except TypeError:
    
    # Alert user to no significant changes in console
    print(f"There are no significant changes with the {stock_name} stock.")