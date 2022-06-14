"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 48
EXERCISE: 48-2 Wikipedia.org
LEVEL: Advanced

"""

from selenium import webdriver

chrome_driver_path = "/Users/eoghy/Desktop/chromedriver"            # Path to Chrome webdriver

driver = webdriver.Chrome(executable_path=chrome_driver_path)       # Create webdriver class object

driver.get("https://en.wikipedia.org/wiki/Main_Page")    # Start the Chrome browser and navigate to a website

articles = driver.find_element_by_css_selector("#articlecount a")       # Get article count element

print(articles.text)        # Print article count to console

driver.quit()       # Quit the browser