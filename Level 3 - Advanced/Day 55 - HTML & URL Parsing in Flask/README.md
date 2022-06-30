# Day 55 HTML & URL Parsing In Flask

## Overview

For Day 55, we will be continuing to work with Flask, HTML and URL's to recreate a higher or lower game.

    Exercise 55-1: Logging Decorator Function

## Project: Higher or Lower

For this project we will be creating a higher or lower game where a user will guess what the random number will be.

### Setup

1. Install [Flask](https://pypi.org/project/Flask/)

### Instructions

1. On the main app route:
   1. Create an h1 tag that says "Guess the number"
   2. Add a Giphy to the page (probably one with numbers)
   3. Sets a random number variable
2. Create another app route:
   1. That takes a number in the URL
   2. Matches the url number with the random number argument
   3. Write h1 tags for each conditional for guesses:
      1. Too High
      2. Too Low
      3. Match

### Comments

The instructions were a little unclear on how the user would make their guess as we aren't using an input. When the user lands on the home page, a random number should be generated.

Then the user will guess the number by added it to the URL path like `/1` and it will check to see if it matches the random number. Each time they land on the home page, a new number should generate.

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/) - Documentation for the Flask package
