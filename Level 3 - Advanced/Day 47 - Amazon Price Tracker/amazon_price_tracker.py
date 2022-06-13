"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 47
PROJECT: Amazon Price Tracker
LEVEL: Advanced

"""

import requests
from bs4 import BeautifulSoup
import pyshorteners
from Modules import emailer

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9"
}

product_link = "https://www.amazon.com/MageGee-Wireless-Rechargeable-Connection-Waterproof/dp/B08LT1TK1Q/?_encoding=UTF8&pd_rd_w=55tNr&content-id=amzn1.sym.bbb6bbd8-d236-47cb-b42f-734cb0cacc1f&pf_rd_p=bbb6bbd8-d236-47cb-b42f-734cb0cacc1f&pf_rd_r=GS0SDKRF06AYN46MZMB9&pd_rd_wg=UgJHe&pd_rd_r=f88f6641-cc76-4065-82ad-837f2dde3466&ref_=pd_gw_ci_mcx_mi"

# Send HTML request to website
r = requests.get(product_link, 
                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
                          "Accept-Language": "en-US,en;q=0.9",
                          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})

at_html = r.text                                                    # Get website data

soup = BeautifulSoup(at_html, "lxml")                               # Create Beautiful Soup class object

get_product_name = soup.find(name="span", id="productTitle")        # Find product name
get_product_name = get_product_name.getText().strip()               # Clean product name string

get_price = soup.find(name="span", class_="a-offscreen")            # Find the price
get_price = get_price.getText().replace('$', '')                    # Clean price string

tiny_url = pyshorteners.Shortener()                                 # Initialize a url shortener object
buy_product = tiny_url.tinyurl.short(product_link)                      # Shorten product url for email alert

# Check for price drop
if float(get_price) < 20.99:
    
    # Format subject
    subject = (f"New low price alert!")
    
    # Format message
    message = (f"The price for the {get_product_name} has dropped.\n\nIt is now {get_price}! Click here to buy: {buy_product}")
    
    emailer.send_Email(subject, message)     # Call function to send email