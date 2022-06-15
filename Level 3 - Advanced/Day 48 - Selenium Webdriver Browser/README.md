# Day 48 Selenium Webdriver Browser

## Overview

For Day 48, we will be learing about Selenium.

      Exercise 48-1: Python.org Webscrape
      Exercise 48-2: Wikipedia.org Webscrape
      Exercise 48-3: The App Brewery Form Fill

## Project: Cookie Clicker

For the Cookie Clicker project, we will be building Selenium code that will play the `Cookie Clicker` game automatically as a bot.

### Setup

1. Install Selenium using [ChromeDriver](https://chromedriver.chromium.org/downloads)

### Instructions

Using [Cookie Cutter](http://orteil.dashnet.org/experiments/cookie/)

   1. Write Selenium code to:
      1. Open to webpage
      2. Repeatedly click on the cookie to earn points as fast as possible
      3. Review store options for upgrades every 5 seconds
         1. Select the most expensive upgrade available
      4. Continue playing until a 5 minute timer runs out

### Comments

This project was a bit out of scope for the training material given. Regardless that we as developers need to learn by doing, if we are not provided sufficient deliverable information, we can't provide.

With this project, the outcome was simple, but getting there was not defined well enough other than some hints to clean strings. One primary struggle was getting the separate element texts together and using them for the game.

#### Issues

- One major issue was that, at some point, there was a `selenium.common.exceptions.StaleElementReferenceException` which did not stop the webdriver, but prevented further upgrades being selected while running.
- The program also did not time out at 5 minutes and close the browser as expected.

### Adjustments

I included error handling as the program will check every 5 seconds for available upgrades. If none are available, then it throws a `ValueError`. For this, I set the exception handling to continue with the program instead of selecting an upgrade.

### Forking

- The `Chromedriver` path will be the direct path to your local chromedriver executable which will launch when called to automate your chrome browser

### Additional Resources

- [ChromeDriver](https://chromedriver.chromium.org/downloads) - Download page for the Google Chrome webdriver executable
- [Selenium Documentation](https://selenium-python.readthedocs.io/) - Documentation for using Selenium
