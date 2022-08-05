# Day 74 Resampling Data & Visualizing Time Series

## Overview

For Day 74, we will be continuing to explore Pandas dataframes, Matplotlib, and moving into visualing time series data.

### Setup

1. Install [Jupyter](https://pypi.org/project/jupyter/)
2. Install [Matplotlib](https://pypi.org/project/matplotlib/)

### Instructions

1. Challenge 1:
   1. Import the data from these CSV files:
      1. Bitcoin Search Trend
      2. Daily Bitcoin Price
      3. Tesla Search Trend vs Price
      4. UE Benefits Sears vs UE Rate 2004-19
   2. Find the shapes of the dataframes
   3. Find the column names
   4. Complete the f-strings to display lowest and highest number in the search data column
   5. Try using `describe()` to see useful stats
   6. Get the periodicity of the data (daily, weekly, monthly)
   7. Discover the meaning of a value of 100 in the Google Trend search popularity
2. Challenge 2:
   1. Check for NaN items in the data
   2. Find the count of missing items
   3. Drop them from the data set
3. Challenge 3:
   1. Check the data type of the entries in the dataframe MONTH or DATE columns
   2. Convert strings to Datetime objects
   3. Validate the conversion was successful
4. Challenge 4:
   1. Use `resample()` to convert the Bitcoin Price data from daily to monthly
   2. Use the last available price of the month for the resampled data
5. Challenge 5:
   1. Using the data from `TESLA Search Trend vs Price.csv`
      1. Plot a line chart with the stock price and search trend as separate lines
   2. Add colors to style the chart
   3. Include:
      1. Increase the figure size (e.g., to 14 by 8)
      2. Increase the font sizes for the labels and the ticks on the x-axis to 14
      3. Rotate the text on the x-axis by 45 degrees
      4. Make the lines on the chart thicker
      5. Add a title that reads 'Tesla Web Search vs Price'
      6. Keep the chart looking sharp by changing the dots-per-inch or [DPI value](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html)
      7. Set minimum and maximum values for the y and x axis
      8. Finally use [plt.show()](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.show.html)
6. Challenge 6:
   1. Using the data from `Bitcoin Search Trend.csv` and `df_btc_monthly`
      1. Plot a line chart with BTC price and search trend as separate lines
   2. Add colors to style the chart
   3. Include:
      1. Modify the chart title to read 'Bitcoin News Search vs Resampled Price'
      2. Change the y-axis label to 'BTC Price'
      3. Change the y- and x-axis limits to improve the appearance
      4. Investigate the [linestyles](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html ) to make the BTC price a dashed line
      5. Investigate the [marker types](https://matplotlib.org/3.2.1/api/markers_api.html) to make the search datapoints little circles
      6. Were big increases in searches for Bitcoin accompanied by big increases in the price?
7. Challenge 7:
   1. Using the data from `UE Benefits Search vs UE Rate 2004-19.csv`
      1. Plot a line chart with unemployment rate and search trend as separate lines
   2. Add colors to style the chart
   3. Include:
      1. Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate
      2. Change the y-axis label to: FRED U/E Rate
      3. Change the axis limits
      4. Add a grey [grid](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.grid.html) to the chart to better see the years and the U/E rate values. Use dashes for the line style
      5. Can you discern any seasonality in the searches? Is there a pattern?
8. Challenge 8:
   1. Read the data from `UE Benefits Search vs UE Rate 2004-20.csv`
   2. Convert the MONTH column to Pandas Datetime objects
   3. Plot the chart as a line chart as in challenge 7

### Comments

This project was fairly simple as the previous, but required some additional research into Matplotlib documentation to learn how to style the charts per requirements. This took a bit longer to work through.
