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

def get_names():
    """ Function used to get names from invite list. """
    # Open file with list of names to invite
    with open("Level 2 - Intermediate/Day 24 - Files, Directories, and Paths/Input/Names/invited_names.txt") as data:
        return data.readlines() # Return names from files as list

def get_letter():
    """ Function used to get letter text from template. """
    # Open file with letter template
    with open("Level 2 - Intermediate/Day 24 - Files, Directories, and Paths/Input/Letters/starting_letter.txt") as data:
        return data.read()  # Return content of letter template as string

def write_letter(name, letter):
    """ Function used to write personalized letter to a new file. """
    # Open or create new file using name parameter
    with open("Level 2 - Intermediate/Day 24 - Files, Directories, and Paths/Output/ReadyToSend/"+name+".txt", mode="w") as invite:
        invite.write(letter.replace("[name],", name + ",")) # Write letter template and replace name holder with name of invitee

invites = get_names() # Get list of invited guests
letter = get_letter() # Get letter template as string

# Write personalized letter for each invitee
for i in invites:
    write_letter(str(i).strip(), letter)    # Call write_letter function and pass name and letter template