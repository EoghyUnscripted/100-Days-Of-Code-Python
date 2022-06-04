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

import smtplib
from decouple import config


class NotificationManager:
    
    def __init__(self):
        self.send_from = config("GMAIL_ACCT")                    # Email address
        self.password = config("GMAIL_PASSWORD")                 # Email password
        self.recipient = []                                      # Create a blank list for email recipients
        self.subject = "New Flight Deals!"                       # Set a subject line
        
    
    def send_Email(self, users, body):
        """ Function used to send an email alert when new deals are found. """
        
        # SMTP Connection Setup

        try:    # Attempt to connect to email server
            
            connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)    # Create a secure SSL connection
            connection.ehlo()   # Identify your email server to the host
            connection.login(user=self.send_from, password=self.password)     # Pass through your credentials
            
        except smtplib.SMTPAuthenticationError:     # If unable to authenticate
            
            print("Could not connect. Please check your authentication settings on your email server.")
            
        except TimeoutError:    # If connection timed out or server did not respond
            
            print("Unable to reach the host server. Please check your SSL and port settings.")
            
        else:   # Set up email content

            print("Sending email...")
            
            self.recipient = [user['email'] for user in users]
            
            # Structure the body content
            message = f"Subject: {self.subject}\n\n{body}".format(self.subject, body)    # Structure the body content

            connection.sendmail(from_addr=self.send_from, to_addrs=self.recipient, msg=message)   # Pass data to server for email message
            
        finally:    # Always execute for security
            
            print("Email sent!")
            connection.close()  # Close the connection
