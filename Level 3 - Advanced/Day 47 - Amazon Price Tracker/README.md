# Day 47 Amazon Price Tracker

## Overview

For Day 47, we will continue working with Beautiful Soup to track the price of a product on Amazon.

## Project: Amazon Price Tracker

For this project, we will be using `Beautiful Soup` to scrape a product page on Amazon to check the price and send an email alert when the price drops below a preset value.

### Instructions

Using [Amazon](https://www.amazon.com/):

1. Choose a product to track
2. Use the URL from that site to return the HTML and scrape the price
   1. If the price is below a preset price, send an email alert

### Example Output

Email Alert Message

      The price for the MageGee TS92 Wireless 60% Gaming Keyboard, Compact 61 Keys Rechargeable RGB Backlit Office Keyboard, 2.4G Wireless Connection Waterproof Portable Computer Keyboard for Mac Windows Laptop (Black) has dropped.

      It is now 22.99! Click here to buy: https://tinyurl.com/24j46tu2

### Comments

For this project I chose to a gaming keyboard [MageGee TS92](https://www.amazon.com/MageGee-Wireless-Rechargeable-Connection-Waterproof/dp/B08LT1TK1Q/?_encoding=UTF8&pd_rd_w=55tNr&content-id=amzn1.sym.bbb6bbd8-d236-47cb-b42f-734cb0cacc1f&pf_rd_p=bbb6bbd8-d236-47cb-b42f-734cb0cacc1f&pf_rd_r=GS0SDKRF06AYN46MZMB9&pd_rd_wg=UgJHe&pd_rd_r=f88f6641-cc76-4065-82ad-837f2dde3466&ref_=pd_gw_ci_mcx_mi&th=1) as the tracked product. In order to test, I set the price to `$23.99` to trigger a response.

As seen above, it sent the email successfully.

#### Forking

When forking, you will need to adjust the SMTP settings in `emailer.py` to your own for it to successfully work.

### Additional Resources

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  - Documentation for the Beautiful Soup module
