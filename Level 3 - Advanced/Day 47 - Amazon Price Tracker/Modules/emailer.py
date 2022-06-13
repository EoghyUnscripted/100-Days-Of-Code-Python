"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 47
PROJECT: Amazon Price Tracker
LEVEL: Advanced

"""

import smtplib
from decouple import config

def send_Email(subject, body):
        """ Function used to send an email alert when a product price has dropped below $20.99 on Amazon. """
        
        send_from = config("GMAIL_ACCT")
        password = config("GMAIL_PASSWORD")
        
        # SMTP Connection Setup

        try:    # Attempt to connect to email server
            
            connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)    # Create a secure SSL connection
            connection.ehlo()   # Identify your email server to the host
            connection.login(user=send_from, password=password)     # Pass through your credentials
            
        except smtplib.SMTPAuthenticationError:     # If unable to authenticate
            
            print("Could not connect. Please check your authentication settings on your email server.")
            
        except TimeoutError:    # If connection timed out or server did not respond
            
            print("Unable to reach the host server. Please check your SSL and port settings.")
            
        else:   # Set up email content

            print("Sending email...")
            
            recipient = [config("GMAIL_TO_ADDRESS")]
            
            # Structure the body content
            message = f"Subject: {subject}\n\n{body}".format(subject, body)    # Structure the body content

            connection.sendmail(from_addr=send_from, to_addrs=recipient, msg=message)   # Pass data to server for email message
            
        finally:    # Always execute for security
            
            print("Email sent!")
            connection.close()  # Close the connection