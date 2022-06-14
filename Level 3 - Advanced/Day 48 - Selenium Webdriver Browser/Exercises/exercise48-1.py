"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 48
EXERCISE: 48-1 Python.org
LEVEL: Advanced

"""

from selenium import webdriver

chrome_driver_path = "/Users/eoghy/Desktop/chromedriver"            # Path to Chrome webdriver

driver = webdriver.Chrome(executable_path=chrome_driver_path)       # Create webdriver class object

driver.get("https://www.python.org")    # Start the Chrome browser and navigate to a website

event_dates = driver.find_elements_by_css_selector(".event-widget time")        # Get event dates
event_names = driver.find_elements_by_css_selector(".event-widget li a")        # Get event names

events = {}     # Blank dictionary to merge event date and name

# Loop through returned results
for n in range(len(event_dates)):
    
    # Merge event data and name into dictionary with key value pairs
    events[n] = {
        "date": event_dates[n].text,       # Set date
        "name": event_names[n].text        # Set name
    }

for event in events:
    
    # Write an output string for readable format
    output = events[event]["date"] + " " + events[event]["name"]

    print(output)       # Print events to console

driver.quit()       # Quit the entire browser instance