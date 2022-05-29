# Day 36 Stock Trading News Alert Project

## Overview

For Day 36, we will build off what we learned for the Rain Alert project in day 35 to create a Stock Alerts project.

## Project: Stock Alerts

Using a stock, news and the Twilio API, we will create an sms alert that is sent out when there is a change of 5% or more, which will include related news articles.

### Setup

- [Alpha Vantage](https://www.alphavantage.co) - Sign up to get a free stock API key
- [News API](https://newsapi.org) - Sign up to get a free news API key
- [Twilio Console](https://www.twilio.com) - Sign up to get an Account SID, Auth Token, trial number and credits for testing
- [Twilio-CLI](https://www.twilio.com/docs/twilio-cli/quickstart) - Install the `twilio-cli` package
- You will need a mobile device that you can use to test

### Instructions

1. Write functions to
   1. Check stock prices (i.e. TSLA):
      1. Get the closing stock price from yesterday and the day before
         1. Find the positive difference between the two
            1. `e.g. 40 - 20 = 20`
            2. [W3Schools - abs()](https://www.w3schools.com/python/ref_func_abs.asp)
      2. Get the price difference between the two days
   2. Check stock news:
      1. If there is a 5% increase or decrease between the two days returned from stock function:
         1. Get 3 news articles using an API relating to the stock
   3. Send Twilio SMS:
      1. Send separate Twilio SMS messages for each headline and news brief

### Example Input

#### News API JSON

```js
[
  {
    'source': {
      'id': None,
      'name': 'Electrek'
    },
    'author': 'Fred Lambert',
    'title': 'Podcast: Tesla (TSLA) falls on ESG and Elongate, FSD Beta update, Cadillac Lyriq pricing, and more',
    'description': 'This week on the\xa0Electrek Podcast, we discuss the most popular news in the world of sustainable transport and energy. This week,\xa0we discussed Tesla (TSLA) falling amid an issue with ESG and the Elongate scandal, a FSD Beta update, the Cadillac Lyriq pricing, …',
    'url': 'https://electrek.co/2022/05/20/podcast-tesla-tsla-falls-esg-elongate-fsd-beta-update-cadillac-lyriq-pricing/',
    'urlToImage': 'https://i0.wp.com/electrek.co/wp-content/uploads/sites/3/2017/12/business_card-1.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1',
    'publishedAt': '2022-05-20T19:38:51Z',
    'content': 'This week on the\xa0Electrek Podcast, we discuss the most popular news in the world of sustainable transport and energy. This week,\xa0we discussed Tesla (TSLA) falling amid an issue with ESG and the Elong…'
  },
  {
    'source': {
      'id': None,
      'name': 'Electrek'
    },
    'author': 'Fred Lambert',
    'title': 'Tesla’s stock (TSLA) takes a beating amidst confusion over Twitter acquisition – is Elon selling?',
    'description': 'Tesla’s stock (TSLA) is currently taking a beating and losing over $150 billion in value amidst the confusion around Elon Musk’s Twitter acquisition. The main question on investors’ minds is: is Elon Musk selling Tesla stocks?\n more…\nThe post Tesla’s stock (T…',
    'url': 'https://electrek.co/2022/04/28/tesla-stock-tsla-takes-beating-amid-confusion-twitter-acquisition-elon-selling/',
    'urlToImage': 'https://i0.wp.com/electrek.co/wp-content/uploads/sites/3/2016/01/elon-musk-twitter1.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1',
    'publishedAt': '2022-04-28T14:44:10Z',
    'content': 'Tesla’s stock (TSLA) is currently taking a beating and losing over $150 billion in value amidst the confusion around Elon Musk’s Twitter acquisition. The main question on investors’ minds is: is Elon…'
  }
]
```

### Example Output

>CVNA: 🔺 8%<br />
>Is it Still a Great Decision to Buy Carvana (CVNA) Shares?. <br />
>https://finance.yahoo.com/news/still-great-decision-buy-carvana-142459182.html

Or

>WDAY: 🔻 -6%<br />
>Workday, Inc.'s (WDAY) CEO Aneel Bhusri on Q1 2023 Results - Earnings Call Transcript<br />
>https://seekingalpha.com/article/4514878-workday-inc-s-wday-ceo-aneel-bhusri-on-q1-2023-results-earnings-call-transcript

### Comments

For this project, I chose to omit the `Headline` label. I also removed the brief and replaced it with the url that comes with the data so that you can open and view the article itself. The headline provided enough information that adding the brief seemed redundant as it repeated the headline for the most part.

#### Forking

If you chose to fork this app, please be sure to update the variables in `stock_alerts.py` with your own data. I recommend setting them as environment variables while your code is open to the public.

For example:

```python
import os

api = os.environ['API_KEY']
```

To set your environment variables, open the `terminal` in your editor and navigate to your environment directory. Create each of your variables using the format below:

```sh
export API_KEY="enterYourStringHere"
```

#### Additional Resources

- [How to Set and Get Environment Variables in Python](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5) - This is a great resource to learn how to create persistent environment variables
- [JSON Viewer](http://jsonviewer.stack.hu) - This site is a useful app that converts single line JSON to formatted for readability
