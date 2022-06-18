"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 53
PROJECT: Housing Search Capstone Project
LEVEL: Advanced

"""

from decouple import config
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class HomeSearchBot():
    
    def __init__(self):
        self.chrome_driver_path = config("CHROMEDRIVER")                              # Set Chrome Driver Path
        self.rentals_url = config("ZILLOW_HOUSING_URL")                               # Set URL for Zillow
        self.form_url = config("GOOGLE_HOUSING_URL")                                  # Set URL for Google Form
        
        
    def find_housing(self):
        """ Function used to search housing data from Zillow and store the data into lists using BeautifulSoup. """
        
        listing_addresses = []                                                        # Blank list for addresses
        listing_prices = []                                                           # Blank list for rent prices
        listing_urls = []                                                             # Blank list for listing url
        listing_dict = []                                                             # Blank list for storing whole listing data
        
        # Get data from Zillow
        r = requests.get(self.rentals_url, 
                         headers={
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                            })
                                             
        zillow_html = r.text                                                         # Get the returned text as HTML

        soup = BeautifulSoup(zillow_html, "html.parser")                             # Create Beautiful Soup class object

        #Get listings URLS
        get_urls = soup.select(".list-card-top a")                                   # Find all listing urls
        
        for url in get_urls:                                                         # Check link strings for full url
            
            link = url["href"]                                                       # Set variable with returned url
            
            if "http" not in link:                                                   # If not full link
                
                listing_urls.append(f"https://www.zillow.com{link}")                 # Pre-pend Zillow link and append to list
                
            else:                                                                    # If full link
                
                listing_urls.append(link)                                            # Append to list
                
        # Get listing addresses        
        get_addresses = soup.select(".list-card-addr")                               # Find all listing addresses
        
        listing_addresses = [address.getText() for address in get_addresses]         # Append each address to list
        
        # Get listings prices
        get_prices = soup.select(".list-card-price")                                 # Find all listing prices
        
        listing_prices = [price.getText().split(" ")[0] for price in get_prices]                   # Append each price to list
        
        # Get listing data into dictionary
        for i in range(len(listing_addresses)):
            
            listing_dict.append(
                {
                    "address": listing_addresses[i],
                    "price": listing_prices[i],
                    "url": listing_urls[i]
                })

        return listing_dict
    
    def record_listings(self, listings):
        """ Function used to enter data gathered by BeautifulSoup into Google Form automatically with Selenium. """
        
        driver = webdriver.Chrome(executable_path=self.chrome_driver_path)           # Create webdriver class object
        
        for n in range(len(listings)):
            
            driver.get(self.form_url)                                                    # Navigate to Google Form
        
            time.sleep(3)                                                                # Wait for page to load
            
            # Get question 1 input field, submit address
            q1_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            q1_field.send_keys(listings[n]["address"])
            
            # Get question 2 input field, submit price
            q2_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            q2_field.send_keys(listings[n]["price"])
            
            # Get question 3 input field, submit url
            q3_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            q3_field.send_keys(listings[n]["url"])
            
            time.sleep(3)                                                                # Wait for page to load

            # Submit form            
            submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
            submit_button.click()