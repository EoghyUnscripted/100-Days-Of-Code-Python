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

import smtplib

def send_Email_Notification(iss_location):
    """ Function used to send a new email when ISS is in the sky and visible. """
    
    # NOTE: This setup is using Gmail SMTP. You will want to use the SMTP based on your own email host.
    #       If using Gmail, check your security settings and set up an App Password for enhanced security.
    
    # Variables
    
    send_from = "your@email.com"
    password = "yourPasswordGoesHere"
    recipient = ['recipient@email.com']
    subject = "ISS Tracking Notification"
    message = f"The ISS is at {iss_location}. \n\n Look up to see it!"

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

        # Structure the body content
        message = f"Subject: {subject}\n\n{message}".format(subject, message)    # Structure the body content

        connection.sendmail(from_addr=send_from, to_addrs=recipient, msg=message)   # Pass data to server for email message
        
    finally:    # Always execute for security
        
        connection.close()  # Close the connection