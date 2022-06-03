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

from twilio.rest import Client
from decouple import config


class NotificationManager:
    
    def __init__(self):
        self.account_sid = config("TWILIO_ACCT_SID")
        self.auth_token = config("TWILIO_AUTH_TOKEN")
        self.from_num = config("TWILIO_PHONE")
        self.to_num = config("TWILIO_VERIFIED_PHONE")
        self.body_text = ""
    
    def send_SMS(self, body_text):
        """ Function used to call API to send an SMS message alert. """
        
        client = Client(self.account_sid, self.auth_token)    # Initiate Twilio client

        message = client.messages \
                        .create(
                            body = body_text,          # Message text
                            from_ = self.from_num,     # From Twilio numbert
                            to = self.to_num           # To verified phone number
                        )

        print(message.status)   # Print status message to console
