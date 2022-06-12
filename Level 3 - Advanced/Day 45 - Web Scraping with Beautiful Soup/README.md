# Day 45 Web Scraping with Beautiful Soup

## Overview

For Day 45, we will be using the Python module `Beautiful Soup` for web scraping, which is a module that is used when APIs are not present, or does not provide the data users are seeking.

      Exercise 45-1: HTML parsing with local HTML file
      Exercise 45-1: HTML parsing with a live website

## Project: 100 Movies

For this project, we will be using `Beautiful Soup` to scrape website data to compile a list of 100 movies that we must watch.

### Instructions

Using [Empire Online](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/):

1. Scrape the top 100 movies of all time from the website using Beautiful Soup
2. Generate a text file called `movies.txt`
   1. List the movie titles in ascending order with the top movie being number 1

### Example Output

      1) The Godfather
      2) The Empire Strikes Back
      3) The Dark Knight
      4) The Shawshank Redemption
      ...

### Comments

For this project, I noticed there were some string inconsistencies with the website data in `100_movies.py`. I added a loop to clean the string data for proper output.

### Additional Resources

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  - Documentation for the Beautiful Soup module
