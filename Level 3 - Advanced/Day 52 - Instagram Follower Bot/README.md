# Day 52 Instagram Follower Bot

## Overview

For Day 52, we will be continuing to work with Selenium and working with Instagram.

## Project: Instagram Follower Bot

The project for today will use Selenium to log into Instagram and automatically follow users.

### Setup

1. Sign up for [Instagram](https://www.instagram.com)

### Instructions

#### Code Steps

1. Create a Class called `InstaFollower`
   1. init()
      1. driver - Selenium driver
   2. login() - method to log in to Instagram
   3. find_followers() - method to find followers of a user account
   4. follow() - method to follow users

#### Process Steps

1. Using Selenium, open to [Instagram](https://www.instagram.com)
   1. Call login() to:
      1. Pass username and password
   2. Call find_followers() to:
      1. Navigate to a users page
      2. Click on the followers link to get followers list
   3. Call follow() to:
      1. Loop through all followers on the list and click to follow

### Comments

June 18, 2022

      Still unable to test program or move forward due to the inability to log in or create a new account to use for the test. As I do not want my primary account to be banned, I am chosing to forego this project.

June 17, 2022

      Due to Instagram locking me out from logging in more than a few times in a row to test, I am unable to continue to test the program.

#### Issues

- Instagram made it difficult to test more than a handful of times before nuking my account. Thankfully, I was using a test account instead of my primary.
- Using Selenium to locate dynamic elements has been posing a challenge as xpath's seem to change based on screen size and continues to crash the program with a `NoSuchElementException`.

#### Solutions

- None.

### Forking

- The `Chromedriver` path will be the direct path to your local chromedriver executable which will launch when called to automate your chrome browser

### Additional Resources

- [ChromeDriver](https://chromedriver.chromium.org/downloads) - Download page for the Google Chrome webdriver executable
- [Selenium Documentation](https://selenium-python.readthedocs.io/) - Documentation for using Selenium
