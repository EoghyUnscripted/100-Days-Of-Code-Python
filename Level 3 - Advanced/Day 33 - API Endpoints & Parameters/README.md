# Day 33 API Endpoints & Parameters

## Overview

For Day 33, we will be learning to work with APIs to build an ISS tracker that alerts us when the ISS is above our location.

    Exercise 33-1: Kanye Quotes (API)

## Project: ISS Tracker (API)

Using what we learn during the exercises, we will be building an ISS Tracker using API data for the position of the ISS. We will also use an API to get sunrise/sunset data for our location to determine if it is dark enough to see the ISS in the sky.

### Instructions

1. Set up API calls
   1. Create a get request to pull data from [ISS Position API](http://api.open-notify.org/iss-now.json)
   2. Create a get request to pull data from [Sunrise / Sunset API](https://api.sunrise-sunset.org/json)
2. Create an HTTP response handler using the `requests` module
   1. This should raise an exception when status is not `200: Success`
3. With the API data
   1. Create ISS variables for:
      1. Longitude
      2. Lattitude
   2. Create Sunrise / Sunset variables for:
      1. Sunrise hour - 24H
      2. Sunset hour - 24H
4. Create a variable with local time
5. Write a function to:
   1. Check if ISS location is within +/- 5 degrees of your position
   2. Check if currently dark in your locale
   3. Send an email to yourself to tell you to look up

### Example Output

#### ISS Is Not Nearby

    The ISS is not nearby.

#### ISS Is Nearby: Day Time

    You can't see the ISS right now.

#### ISS Is Nearby: Night Time

`Email Message Example`

    The ISS is at (96.9482, -46.4034) 

    Look up to see it!

### Comments

#### Issues

- One major issue I had along the way was converting UTC to local time zone
- Also, the API data for sunrise and sunset time does not account for DST

#### Solutions

- Local Time: I converted local time to UTC which made it easier for accurate sunrise and sunset comparisons
- DST: To solve this issue, I tested the local date agaist DST in the US and converted the local UTC time to DST time

#### Demo Notes

There is no demo available.
