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

from Modules import emailer, tracker

# Starting variables

latitude, longitude = 47.606209, -122.332069     # Set your latitude and longitude
        
def is_ISS_Viewable():
    """ Function used to check if ISS is near given latitude and longitude and is dark enough to view. """
    
    location = (longitude, latitude)    # Gets your location as a tuple
    iss_location = tracker.where_is_ISS()   # Get the location of the ISS as a tuple
    iss_lat_range = [int((iss_location[1] - 5)), int((iss_location[1] + 5))]   # Get +/- latitude range
    iss_lng_range = [int((iss_location[0] - 5)), int((iss_location[0] + 5))]   # Get +/- 5 longitude range
    
    # Check if ISS is within +/- 5 degrees of local position
    if location[0] in range(iss_lng_range[0], iss_lng_range[1]) and location[1] in range(iss_lat_range[0], iss_lat_range[1]):
            
        if tracker.is_it_night(longitude, latitude):   # If it is night time and can be viewed

            emailer.send_Email_Notification(iss_location)   # Call function to send email notification
        
        else:   # If it is day time and can't be viewed
        
            print("You can't see the ISS right now.")  # Print message to console

    else:   # If the ISS is not within +/- 5 degrees of local position
        
        print("The ISS is not nearby.")     # Print message to console


is_ISS_Viewable()   # Initial function call
