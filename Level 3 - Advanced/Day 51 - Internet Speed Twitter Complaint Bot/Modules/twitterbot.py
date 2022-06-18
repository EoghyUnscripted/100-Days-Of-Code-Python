"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 51
PROJECT: Internet Speed Twitter Complaint Bot
LEVEL: Advanced

"""


from decouple import config
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class InternetSpeetTwitterBot():
    
    def __init__(self):
        self.upload = 10                                                              # Set upload speed
        self.download = 100                                                           # Set download speed
        self.contract_upload_speed = 15                                               # Set contract upload speed
        self.contract_download_speed = 300                                            # Set contract download speed
        self.low_speeds = True                                                        # Set low speed boolean
        self.chrome_driver_path = config("CHROMEDRIVER")                              # Set Chrome Driver Path
        self.speed_test_url = "https://www.speedtest.net"                             # Set URL for speed test
        self.twitter_url = "https://www.twitter.com"                                  # Set URL for Twitter
        self.twitter_username = config("TWITTER_USERNAME")                            # Set Twitter username
        self.twitter_password = config("TWITTER_PASSWORD")                            # Set Twitter password
        self.isp_twitter_handle = config("ISP_HANDLE")                                # Set ISP Twitter Handle
        self.isp_locale = config("ISP_LOCALE")                                        # Set ISP service area
        self.twitter_message = "Default"                                              # Set Twitter message
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)       # Create webdriver class object
        
    def get_internet_speed(self):
        """ Function used to test internet speed. """
        
        self.driver.get(self.speed_test_url)                            # Start the Chrome browser and navigate speed test
        time.sleep(5)                                                   # Sleep to wait for page to load
        
        go_button = self.driver.find_element_by_class_name("js-start-test")     # Get go button element
        go_button.click()                                                       # Click go button
        
        time.sleep(60)                                                  # Sleep to wait for speed test to finish
        
        self.download = int(self.driver.find_element_by_class_name("download-speed").text.split(".")[0])    # Get download speed as int
        self.upload = int(self.driver.find_element_by_class_name("upload-speed").text.split(".")[0])        # Get upload speed as int
            
        # Check if download or upload speed is lower than contract guarantee
        if self.contract_download_speed > self.download or self.contract_upload_speed > self.upload:
            
            self.low_speeds = True                                      # Set boolean to True
            
            # Format twitter message
            self.twitter_message = (f"Hey, {self.isp_twitter_handle}, why are my speeds at {self.download}/{self.upload} when "
                                    + f"my contract says I should have a guaranteed {self.contract_download_speed}/{self.contract_upload_speed} "
                                    + f"in {self.isp_locale}?")

            return self.low_speeds
            
        else:   # If nominal speeds
            
            print(f"Your speed is nominal and within contract at {self.download}/{self.upload}.")       # Output nominal speeds message to console
            self.driver.quit()                                                                          # Quit browser
            
            return self.low_speeds
    
    def tweet_to_provider(self):
        """ Function used to log into Twitter and Tweet complaint message to local ISP. """
        
        self.driver.get(self.twitter_url)                               # Navigate to Twitter
        time.sleep(5)                                                   # Sleep to wait for page to load
        
        # Get login button
        login_button = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
        login_button.click()                                            # Click to login
        
        time.sleep(5)                                                   # Sleep to wait for page to load
        
        username_input = self.driver.find_element_by_name("text")       # Get username element
        username_input.click()                                          # Click into field
        username_input.send_keys(self.twitter_username)                 # Send username
        username_input.send_keys(Keys.ENTER)                            # Enter to continue
        
        time.sleep(5)                                                   # Sleep to wait for page to load
        
        password_input = self.driver.find_element_by_name("password")   # Get password element
        password_input.click()                                          # Click into field
        password_input.send_keys(self.twitter_password)                 # Send password
        password_input.send_keys(Keys.ENTER)                            # Enter to continue
        
        time.sleep(5)                                                   # Sleep to wait for page to load
        
        # Get root element for tweet box
        compose_root = self.driver.find_element_by_xpath("//*[text()='Tweet']")
        compose_root.click()                                            # Click into field
        
        time.sleep(3)                                                   # Sleep to wait for page to load
        
        # Get tweet box element to type message
        tweet_message = self.driver.find_element_by_class_name("public-DraftStyleDefault-ltr")
        tweet_message.send_keys(self.twitter_message)                   # Send tweet message
        
        time.sleep(5)                                                   # Sleep to wait for page to load
        
        # Get tweet submit button
        tweet_send = self.driver.find_element_by_xpath("//*[text()='Tweet']")
        tweet_send.click()                                              # Click button to submit
        
        time.sleep(5)                                                   # Sleep to wait for page to load
        
        self.driver.quit()                                              # Quit browser