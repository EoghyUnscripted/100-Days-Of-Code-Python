"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 24
PROJECT: Mail Merge
LEVEL: Intermediate

"""

from Modules import invites

# Get invite names as list, letter template as string, and output file directory as string
invitees = invites.get_names("Level 2 - Intermediate/Day 24 - Files, Directories, and Paths/Input/Names/invited_names.txt")
letter = invites.get_letter("Level 2 - Intermediate/Day 24 - Files, Directories, and Paths/Input/Letters/starting_letter.txt")
output_dir = "Level 2 - Intermediate/Day 24 - Files, Directories, and Paths/Output/ReadyToSend/"

invites.write_letter(invitees, letter, output_dir)   # Call write_letter function and pass name, letter template, and directory location