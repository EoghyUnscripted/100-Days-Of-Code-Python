# Day 49 Automating Job Applications on LinkedIn

## Overview

For Day 49, we will be using Selenium to automate job applications.

## Project: LinkedIn Job App

The project for today will use Selenium to search for "Easy Apply" jobs on LinkedIn and automatically submit applications.

### Setup

1. Install Selenium using [ChromeDriver](https://chromedriver.chromium.org/downloads)
2. Sign up for a free account on [LinkedIn](http://www.linkedin.com)
   1. Fill in your profile
   2. Upload your resume in your settings menu
      1. Settings & Privacy → Job Application Settings

### Instructions

***NOTE: Instructions have been updated for the new LinkedIn layout***

Using [LinkedIn](http://www.linkedin.com), sign in.

   1. Go to the Jobs tab
      1. Enter the job and location you are interested in and search
      2. On the next page, select filters:
         1. Easy Apply
         2. Any other filters you wish to select (i.e Full time, Remote, etc)
      3. Copy the URL once you are finished
   2. Create Selenium code to open the Chrome browser to your link
      1. Create additional Selenium code to automatically log in
         1. If you are already logged in, log out to get the login modal to appear
   3. Create Selenium code to find all of the job listings on the first page
      1. Loop through and check if single page application
         1. Skip the multi-page applications and continue to the next
         2. Apply to all of the single page applications

### Comments

I created two project files for day 48 as I did not want to actually apply to all of the jobs. Instead, I chose to create a second file to save the jobs, instead.

- `linkedin_job_app_apply` - this project file will go through and apply to the jobs
- `linkedin_job_app_save` - this project file will go through and save the jobs

#### Issues

- One major issue is that you do not get to pick and choose the jobs you apply to, which can cause some awkward conversations if you get a call for a job you don't remember applying to.
- Another issue is that, with the `linkedin_job_app_save` file, if you already saved the jobs, it will unsave them. A non-issue for testing.

### Additional Resources

- [ChromeDriver](https://chromedriver.chromium.org/downloads) - Download page for the Google Chrome webdriver executable
- [Selenium Documentation](https://selenium-python.readthedocs.io/) - Documentation for using Selenium
