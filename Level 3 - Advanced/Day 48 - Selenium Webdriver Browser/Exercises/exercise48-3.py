"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 48
EXERCISE: 48-3 App Brewery Newsletter
LEVEL: Advanced

"""

from selenium import webdriver

chrome_driver_path = "/Users/eoghy/Desktop/chromedriver"            # Path to Chrome webdriver

driver = webdriver.Chrome(executable_path=chrome_driver_path)       # Create webdriver class object

driver.get("http://secure-retreat-92358.herokuapp.com/")    # Start the Chrome browser and navigate to a website

fname = driver.find_element_by_class_name("top")     # Find the First Name element
fname.click()       # Get input focus
fname.send_keys("FirstName")       # Send first name

lname = driver.find_element_by_class_name("middle")     # Find the Last Name element
lname.click()       # Get input focus
lname.send_keys("LastName")       # Send last name

email = driver.find_element_by_class_name("bottom")     # Find the Email element
email.click()       # Get input focus
email.send_keys("email@domain.com")       # Send email

submit = driver.find_element_by_class_name("btn")       # Find Sign Up button
submit.click()      # Click button
