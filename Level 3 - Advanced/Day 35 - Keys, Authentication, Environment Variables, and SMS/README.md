# Day 35 Keys, Authentication, Environment Variables, and SMS

## Overview

For Day 35, we will be continuing to work with APIs and working with Twilio to send SMS messages. We will also be looking into authentication and environment variables.

## Project: Rain Alert

We will be working with Twilio API to send an SMS message to ourselves whenever it is going to rain.

### Setup

- [Open Weather Map](https://home.openweathermap.org) - Sign up to get a free API key
- [Twilio Console](https://www.twilio.com) - Sign up to get an Account SID, Auth Token, trial number and credits for testing
- [Twilio-CLI](https://www.twilio.com/docs/twilio-cli/quickstart) - Install the `twilio-cli` package
- You will need a mobile device that you can use to test

### Instructions

1. Create API call functions
   1. Pull hourly weather data from Open Weather Map
      1. Convert data to JSON
      2. Get a list of the conditions for the next 12 hours
      3. Loop through and check if condition `id < 700`
   2. Connect to Twilio API
      1. Create a default sms message object
      2. Pass your Twilio variables into the function:
         1. `Account_SID` - Get this from your Twilio Console
         2. `Auth_Token`  - Get this from your Twilio Console
         3. `from_num`    - Get this from your Twilio Console
         4. `to_num`      - This is your Twilio verified number
         5. `body_text`   - The sms message content
2. Use [Python Anywhere](https://www.pythonanywhere.com) to host your code (optional)
   1. Set the app to run automatically at a set time every day
   2. Use environment variables to hide keys and tokens
      1. You will need to export each environment variable into your run command

#### Twilio Code

```python
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)
```

### Comments

I chose not to automate this app on Python Anywhere as I have no use for it. However, I chose to use environment variables in my source code to upload to GitHub. Not that anyone is interested in stealing an API key for some weather data.

#### Forking

If you chose to fork this app, please be sure to update the variables in `rain_alert.py` with your own data. I recommend setting them as environment variables while your code is open to the public.

For example:

```python
import os

api = os.environ['API_KEY']
```

To set your environment variables, open the `terminal` in your editor and navigate to your environment directory. Create each of your variables using the format below:

```sh
export API_KEY="enterYourStringHere"
```
