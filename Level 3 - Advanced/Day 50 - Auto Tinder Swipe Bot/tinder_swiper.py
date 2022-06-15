"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 50
PROJECT: Tinder Swiper
LEVEL: Advanced

"""

import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

username = config("TINDER_USERNAME")       # Set username
password = config("TINDER_PASSOWRD")       # Set password
tinder_url = "https://tinder.com"          # Url to open

chrome_driver_path = config("CHROMEDRIVER")                         # Path to Chrome webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)       # Create webdriver class object

driver.get(tinder_url)                     # Start the Chrome browser and navigate to a website

time.sleep(3)               # Sleep to wait for page to load

""" Log In """

# Find log in button
login_button = driver.find_element_by_xpath("//*[@id='t546383398']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_button.click()        # Click to open login modal

time.sleep(1)               # Sleep to wait for page to load

# Find log in with Facebook button
facebook_button = driver.find_element_by_xpath("//*[@id='t-1181997678']/div/div/div[1]/div/div/div[3]/span/div[2]/button")
facebook_button.click()     # Click to log in with Facebook

### Facebook login opens to a new window ###

time.sleep(1)               # Sleep to wait for page to load

base_window = driver.window_handles[0]          # Set parent window
fb_login_window = driver.window_handles[1]      # Set child window

### Switch to Facebook login Window ###

driver.switch_to.window(fb_login_window)        # Switch to new window

# NOTE: Normal users keep Facebook logged in so we will use error handling to test and log in if not already

try: 

    # Find continue button to login with Facebook
    fb_login_button = driver.find_element_by_xpath("//*[@id='mount_0_0_Xy']/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div/div/div[2]")
    fb_login_button.click()     # Click to continue to log in with Facebook
    
except NoSuchElementException:
    
    # If not logged in on Facebook
    
    email_input = driver.find_element_by_id("email")       # Find email input
    email_input.click()                                     # Click into input field
    email_input.send_keys(username)                         # Send username to input field
    
    password_input = driver.find_element_by_id("pass")     # Find password input
    password_input.click()                                  # Click into input field
    password_input.send_keys(password)                      # Send password to input field
    password_input.send_keys(Keys.ENTER)                    # Submit form

driver.switch_to.window(base_window)        # Return to parent window

time.sleep(10)                               # Sleep to allow page to load

""" Pop Up Handling """

try:

    # Allow location
    allow_location_button = driver.find_element_by_xpath("//*[@id='t-1181997678']/div/div/div/div/div[3]/button[1]")
    allow_location_button.click()               # Click to accept

    #Disallow notifications
    notifications_button = driver.find_element_by_xpath("//*[@id='t-1181997678']/div/div/div/div/div[3]/button[1]")
    notifications_button.click()                # Click to reject

    #Allow cookies
    cookies = driver.find_element_by_xpath("//*[@id='t546383398']/div/div[2]/div/div/div[1]/div[1]/button")
    cookies.click()                             # Click to accept
    
except NoSuchElementException:
    
    print("No pop-ups found.")
    
# NOTE: For the Tinder free version, only 100 likes are allowed a day

time.sleep(10)                              # Sleep to wait for likes to load

for n in range(100):

    time.sleep(1)                           # Sleep timer between likes to prevent being blocked

    try:
        
        # Click into user
        user_details = driver.find_element_by_xpath("//*[@id='t546383398']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div[3]/button")
        user_details.click()                # Click to view user details
        
        # Find the like button
        like_button = driver.find_element_by_xpath("//*[@id='t546383398']/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[4]/button")
        like_button.click()                 # Click to like

    
    except ElementClickInterceptedException:        # When a match is detected
        
        try:
            
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")       # Get match popup element
            match_popup.click()                     # Click to clear

        except NoSuchElementException:              # Like button hasn't loaded
            
            time.sleep(2)                           # Sleep to wait for page to load
    
    except NoSuchElementException:              # Like button hasn't loaded
    
        time.sleep(2)                           # Sleep to wait for page to load


driver.quit()