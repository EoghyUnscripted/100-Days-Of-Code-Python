"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 48
PROJECT: Cookie Clicker
LEVEL: Advanced

"""

from selenium import webdriver
import time


# Path to Chrome webdriver
chrome_driver_path = "/Users/eoghy/Desktop/chromedriver"

# Create webdriver class object
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Start the Chrome browser and navigate to a website
driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 60*5        # 5 minutes game timer
timer = time.time() + 5             # 5 second store timer

cookies = driver.find_element_by_id("cookie")                   # Find cookie element

items = driver.find_elements_by_css_selector("#store div")      # Find store elements
item_ids = [item.get_attribute("id") for item in items]         # Insert store element id's in a list

# Set loop for clicker and game timeout
while True:

    cookies.click()     # Click cookie element

    # Every 5 seconds
    if time.time() > timer:

        # Check upgrades
        upgrade_prices = driver.find_elements_by_css_selector("#store b")    # Get upgrade elements and price
        item_prices = []    # Empty list to hold current prices

        # Get upgrade elements
        for price in upgrade_prices:

            upgrade_text = price.text   # Get the upgrade label string to convert to integer

            if upgrade_text != "":      # If not blank (greyed elements)

                
                item_cost = int(upgrade_text.split("-")[1].strip().replace(",", ""))    # Get cost string as integer
                item_prices.append(item_cost)       # Append cost to the list

        cookie_upgrades = {}       # Dictionary to store available upgrades

        # Crate dictionary with store items and their prices
        for n in range(len(item_prices)):

            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current wallet balance
        money_element = driver.find_element_by_id("money").text
        
        if "," in money_element:
            
            # Clean string for int conversion
            money_element = money_element.replace(",", "")
            
        cookie_count = int(money_element)   # Update wallet count

        # Find upgrades that we can currently afford
        affordable_upgrades = {}    # Dictionary to store available upgrades we can purchase
        
        for cost, id in cookie_upgrades.items():
            
            if cookie_count > cost:     # Check if cookie count is above upgrade cost
                
                affordable_upgrades[cost] = id      # Set element id

        # Purchase the most expensive affordable upgrade
        
        try:
            
            highest_price_affordable_upgrade = max(affordable_upgrades)     # Get the most expensive upgrade
            
        except ValueError:
            
            continue    # Keep the game going even if no upgrades avail
        
        else:
            
            print(highest_price_affordable_upgrade)     # Print to console
            
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]      # Set element id to point to

            driver.find_element_by_id(to_purchase_id).click()       # Click for upgrade
        
        finally:
            
            timeout = time.time() + 5       # Add 5 seconds to the timer

    # Time out after 5 minutes, break loop
    if time.time() > timeout:
        
        cookies_ps = driver.find_element_by_id("cps").text      # Get cookies/second result
        print(cookies_ps)       # Print to console
        
        break       # End loop

driver.quit()       # Quit the entire browser instance
