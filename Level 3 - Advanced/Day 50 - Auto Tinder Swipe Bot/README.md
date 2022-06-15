# Day 50 Auto Tinder Swipe Bot

## Overview

For Day 50, we will be continuing to work with Selenium and working wiht Tinder.

## Project: Auto Tinder Swipe Bot

The project for today will use Selenium to log in to Tinder and auto swipe.

### Setup

1. Sign up for [Tinder](https://tinder.com)

### Instructions

1. Using Selenium, open to Tinder.com
   1. Click the log in button
   2. Select "Log In With Facebook"
      1. Pass in your credentials
   3. When Tinder loads
      1. Use Selenium to:
         1. Click enable location
         2. Click enable notifications
         3. Click allow cookies
   4. Loop code to locate and click the like button
   5. If a match:
      1. Write an exception handler to close the modal
      2. Continue with likes until you hit your daily limit (free version)

### Comments

It took a while to get this to work as the browser settings kept changing the webpage layouts depending on saved data or if logged in on Tinder or Facebook already.

Overall, I would never really use this bot. It works to meet the requirements of the assignment, but not a usefull tool.

#### Issues

- Tinder makes it a bit difficult to identify elements, even when using the xpath.
- The program initially kept crashing for `NoSuchElementException` as it was unable to locate the like button.
- Tinder pop-ups interfere with the app which would require much more code to handle.

#### Solutions

- As the program couldn't locate the like button, I opted to select the `(i)` button first, and clicking the like button in the details screen. This option worked instead of throwing an exception.
- I was able to work around some of the `NoSuchElementException` errors by setting the program to sleep and manually clicking when it had trouble finding elements. This seemed to allow it to work on it's own for a couple "likes", but would then stop, again.

### Forking

- The `Chromedriver` path will be the direct path to your local chromedriver executable which will launch when called to automate your chrome browser

### Additional Resources

- [ChromeDriver](https://chromedriver.chromium.org/downloads) - Download page for the Google Chrome webdriver executable
- [Selenium Documentation](https://selenium-python.readthedocs.io/) - Documentation for using Selenium
