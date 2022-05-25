"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 32
PROJECT: Automated Birthday Emailer
LEVEL: Advanced

"""

import smtplib    

def send_Birthday_Wishes(send_from, password, recipient, subject, message):
    """ Function used to send a new email with a birthday message. """
    
    # NOTE: This setup is using Gmail SMTP. You will want to use the SMTP based on your own email host.
    #       If using Gmail, check your security settings and set up an App Password for enhanced security.

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
        