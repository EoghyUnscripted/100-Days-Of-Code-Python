"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 45
PROJECT: 100 Movies
LEVEL: Advanced

"""

import requests
from bs4 import BeautifulSoup

# Get website data
r = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

# Get the returned text as HTML
eo_html = r.text

# Create Beautiful Soup class object
soup = BeautifulSoup(eo_html, "html.parser")

# Gather the movie names and ranks
get_titles = soup.find_all(name="h3", class_="title")

# Create a list of the movie titles
movie_titles = []
movie_titles = [movie_titles.append(title.getText()) for title in get_titles]

# Reverse the order to ascending
movie_titles.reverse()
    
# Loop through list to clean string data
for i in range(len(movie_titles) - 1):
    
    old_string = str(movie_titles[i])   # Get each string
    
    if ":" in old_string:   # Check for colons
        
        new_string = old_string.replace(":", ")")   # Replace with rounded bracket
        movie_titles[i] = new_string                # Update the element in the list

# Write list to file from 1 - 100
with open("Level 3 - Advanced/Day 45 - Web Scraping with Beautiful Soup/Output/movies.txt", "w") as f:
    
    # Loop through lines in list
    for row in movie_titles:
        f.write(f"{row}\n")     # Write each line to file