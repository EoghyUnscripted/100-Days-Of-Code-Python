"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 52
PROJECT: Instagram Follower Bot
LEVEL: Advanced

"""

from Modules import instagram_bot


new_bot = instagram_bot.InstaFollower()

new_bot.login()

new_bot.find_followers()
