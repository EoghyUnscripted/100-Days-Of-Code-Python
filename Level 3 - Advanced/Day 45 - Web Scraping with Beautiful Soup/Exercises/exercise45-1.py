"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 45
EXERCISE: 45-1 Parsing Local HMTL
LEVEL: Advanced

"""

from bs4 import BeautifulSoup

# Open HTML file and get contents
with open("Level 3 - Advanced/Day 45 - Web Scraping with Beautiful Soup/Exercises/Modules/local.html", "r", encoding='utf-8') as f:
    contents = f.read()
    
# Create a new Beautiful Soup class object
soup = BeautifulSoup(contents, "html.parser")

# Get first anchor tag
print(soup.a)

# Get string from anchor tag
print(soup.a.string)

# Find all anchor tags
print(soup.findAll(name="a"))

# Get all href links in the a tags
for tag in soup.findAll(name="a"):
    print(tag.get("href"))
    
# Get a specific element
print(soup.find(name="h1", id="name"))