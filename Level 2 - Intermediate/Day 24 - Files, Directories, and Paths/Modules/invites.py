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

def get_names(file):
    """ Function used to get names from invite list. """
    # Open file with list of names to invite
    with open(file) as data:
        return data.readlines() # Return names from file as list

def get_letter(file):
    """ Function used to get letter text from template. """
    # Open file with letter template
    with open(file) as data:
        return data.read()  # Return content of letter template as string

def write_letter(name, letter, file_dir):
    """ Function used to write personalized letter to a new file. """
    for n in name:  # For each name passed
        
        n = str(n).strip()  # Cleans variable
        
        # Open or create new file using name parameter
        with open(file_dir+"letter_for_"+n+".txt", mode="w") as invite:
            invite.write(letter.replace("[name]", n)) # Write letter template and replace name holder with name of invitee