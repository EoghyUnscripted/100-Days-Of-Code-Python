# Day 51 Internet Speed Twitter Complaint Bot

## Overview

For Day 51, we will be continuing to work with Selenium and working with Twitter.

## Project: Auto Tinder Swipe Bot

The project for today will use Selenium to check the current internet speeds from our ISP and tweet to Twitter when it is below our contracted guaranteed speeds.

### Setup

1. Sign up for [Twitter](https://www.twitter.com)

### Instructions

#### Code Steps

1. Create a Class called `InternetSpeedTwitterBot`
   1. init()
      1. up - variable to store the upload speed
      2. down - variable to store the download speed
      3. driver - Selenium driver
   2. get_internet_speed() - method to get and set the internet upload and download speed
   3. tweet_to_provider() - method to send a tweet to the provider with complaint

#### Process Steps

1. Using Selenium, open to [Speedtest By Okla](https://www.speedtest.net)
   1. Click the `Go` button
   2. Once the test has finished, use a `InternetSpeedTwitterBot` class to:
      1. `get_internet_speed()`
         1. Get upload and download speeds and store into variables
         2. Compare speed to contract guarantee speeds
      2. `tweet_to_provider()`
         1. If speeds are lower than contracted guarantee, call this function
         2. Creates twitter message with current speeds and contract speeds
   3. Load Twitter
      1. Use Selenium to:
         1. Login
         2. Create a tweet
         3. Post tweet

### Comments

This project was fairly easy to produce with a couple of exceptions. Using a class object was much more useful to me as a developer and made the process flow much easier.

#### Issues

- The primary issue I had was accessing the Twitter elements to create a new tweet and post it. I was not the only one that had issues given that the tutorial was put together prior to Twitter UI updates.

#### Solution

- I was able to locate feedback from another student that took the course and was able to use JavaScript elements to identify the elements needed to create and post a tweet and I used those identifiers for my project to help me to complete my code.

### Forking

- The `Chromedriver` path will be the direct path to your local chromedriver executable which will launch when called to automate your chrome browser

### Additional Resources

- [ChromeDriver](https://chromedriver.chromium.org/downloads) - Download page for the Google Chrome webdriver executable
- [Selenium Documentation](https://selenium-python.readthedocs.io/) - Documentation for using Selenium
