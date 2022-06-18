"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 53
PROJECT: Housing Search Capstone Project
LEVEL: Advanced

"""

from Modules import house_finder

# Create HomeSearchBot class object
new_home = house_finder.HomeSearchBot()

# Create a variable with the return dictionary from search
listings = new_home.find_housing()

# Call function to record listing data to Google form
new_home.record_listings(listings)
