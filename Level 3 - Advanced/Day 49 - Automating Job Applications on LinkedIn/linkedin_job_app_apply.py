"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 49
PROJECT: LinkedIn Job App
LEVEL: Advanced

"""

import time
from decouple import config
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


li_username = config("LINKEDIN_USERNAME")       # Set username
li_password = config("LINKEDIN_PASSOWRD")       # Set password

# LinkedIn job search url with job filters
linkedin_search_url = "https://www.linkedin.com/jobs/search/?distance=25.0&f_AL=true&f_E=2&f_JT=F&f_TPR=r604800&f_WT=2&geoId=103644278&keywords=python%20developer"

chrome_driver_path = "/Users/eoghy/Desktop/chromedriver"        # Path to Chrome webdriver

driver = webdriver.Chrome(executable_path=chrome_driver_path)       # Create webdriver class object

driver.get(linkedin_search_url)     # Start the Chrome browser and navigate to a website

time.sleep(1)       # Sleep to wait for page load

sign_in_button = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")      # Find sign in button
sign_in_button.click()      # Click to sign in

time.sleep(1)       # Sleep to wait for page load

username_input = driver.find_element_by_css_selector("div #username")     # Get username input element
username_input.click()                                                    # Click element to type
username_input.send_keys(li_username)                                     # Enter username

password_input = driver.find_element_by_css_selector("div #password")     # Get password input element
password_input.click()                                                    # Click element to type
password_input.send_keys(li_password)                                     # Enter password

# Find the sign in button
log_in_button = driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
log_in_button.click()       # Click to sign in

time.sleep(1)       # Sleep to wait for page load

# Get all job listings
job_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

# Loop through each listing and save jobs
for job in job_listings:
    
    print(f"Getting job {job.text}...")     # Output status message to console
    job.click()                             # Select job
    time.sleep(1)                           # Sleep to wait for page to update

    try:
        
        print(f"Applying...")               # Output status message to console
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")      # Get apply button
        apply_button.click()                # Click to apply
        
        submit_button = driver.find_element_by_css_selector("footer button")   # Get submit button
        
        # If app is multi-page
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            
            # Find close button on app
            close_button = driver.find_element_by_class_name("artdeco-modal_dismiss")
            close_button.click()            # Click to close app
            
            time.sleep(1)                   # Sleep to wait for confirmation dialog to load
            
            # Find discard confirmation button
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-button")[1]
            discard_button.click()          # Click to confirm discard app
            
            continue                        # Skip application
    
        else:
            
             submit_button.click()          # Click to submit application
        
    except NoSuchElementException:
        
        continue                            # Skip if no apply button
    
driver.quit()                               # Quit browser
