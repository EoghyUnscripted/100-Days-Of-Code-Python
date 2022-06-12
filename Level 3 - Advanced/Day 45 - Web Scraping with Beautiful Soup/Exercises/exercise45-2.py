"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 45
EXERCISE: 45-2 Parsing Live Website HMTL
LEVEL: Advanced

"""

import requests
from bs4 import BeautifulSoup

# Get website data
r = requests.get("https://news.ycombinator.com")

# Get the returned text as HTML
yc_web_page = r.text

# Create Beautiful Soup class object
soup = BeautifulSoup(yc_web_page, "html.parser")

# Set blank lists to store all article texts, upvotes and links
article_texts = []
article_links = []

# Get all article names, links, and upvotes
articles = soup.find_all(name="a", class_="titlelink")
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

for tag in articles:
    
    text = tag.getText()            # Get article name
    article_texts.append(text)      # Append to list
    
    link = tag.get("href")          # Get article link
    article_links.append(link)      # Append to list


# Find the id of the highest number of upvotes
highest_rank_id = article_upvotes.index(max(article_upvotes))

# Print Title and Link of the article with the highest number of upvotes
article = article_texts[highest_rank_id] + " " + article_links[highest_rank_id]
print(article)