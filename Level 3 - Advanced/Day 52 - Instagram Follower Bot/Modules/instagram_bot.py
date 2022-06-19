"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 52
PROJECT: Instagram Follower Bot
LEVEL: Advanced

"""


from decouple import config
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class InstaFollower():
    
    def __init__(self):
        self.chrome_driver_path = config("CHROMEDRIVER")                              # Set Chrome Driver Path
        self.instagram_url = "https://www.instagram.com/accounts/login/"              # Set URL for Instagram
        self.instagram_username = config("INSTAGRAM_USERNAME")                        # Set Instagram username
        self.instagram_password = config("INSTAGRAM_PASSWORD")                        # Set Instagram password
        self.test_url = config("IG_ACCOUNT_URL")                                      # Set Instagram account URL for following
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)       # Create webdriver class object
        
    
    def login(self):
        
        self.driver.get(self.instagram_url)                                           # Open Chrome to Instagram
        self.driver.maximize_window()
        
        time.sleep(5)                                                                 # Wait for page to load
        
        username_field = self.driver.find_element_by_name("username")                 # Get username field
        username_field.click()                                                        # Click into field
        username_field.send_keys(self.instagram_username)                             # Send username
        
        time.sleep(1)                                                                 # Wait for page to load
        
        password_field = self.driver.find_element_by_name("password")                 # Get password field
        password_field.click()                                                        # Click into field
        password_field.send_keys(self.instagram_password)                             # Send password
        
        time.sleep(1)                                                                 # Wait for page to load
        
        password_field.send_keys(Keys.ENTER)                                          # Send ENTER command to login
        
        time.sleep(5)                                                                 # Wait for page to load
        
    
    def find_followers(self):
        
        self.driver.get(self.test_url)                                                # Navigate to Instagram user URL
        
        time.sleep(5)                                                                 # Wait for page to load
        
        # XPath to Followers button on user profile - Selenium returns NoSuchElementException
        self.driver.find_element_by_xpath("//*[@id='mount_0_0_cH']/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        
        # NOTE: Unable to continue testing due to IG security blocking test account from logging in.
        #       Uable to create a new test account to continue working.
        #       Will not be attempting to finish this project as I do not want my primary account to be blocked as well.

    def follow(self):
        """ Function used to follow all users. """
        
        pass