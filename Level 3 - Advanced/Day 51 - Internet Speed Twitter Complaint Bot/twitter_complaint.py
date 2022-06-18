"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 51
PROJECT: Internet Speed Twitter Complaint Bot
LEVEL: Advanced

"""

from Modules import twitterbot


# Initiate new bot class object
new_bot = twitterbot.InternetSpeetTwitterBot()

# Check if internet speed is low
if new_bot.get_internet_speed():

    # Send tweet to provider
    new_bot.tweet_to_provider()

else:
    
    # Close browser
    new_bot.driver.quit()