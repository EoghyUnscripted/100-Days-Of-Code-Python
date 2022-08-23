# Day 75 Plotly Charts & Analyzin Android App Store

## Overview

For Day 75, we will be working more with plotly and large data.

### Setup

1. Install [Jupyter](https://pypi.org/project/jupyter/)
2. Install [Matplotlib](https://pypi.org/project/matplotlib/)

### Instructions

1. Challenge 1:
   1. Import the data from the provided CSV file `apps.csv`
   2. Find the shape of the dataframe
   3. Find the column names
   4. Get a random sample of 5 rows using `sample()`
   5. Drop unused columns:
      1. Last_Updated
      2. Android_Ver
2. Challenge 2:
   1. With the new dataframe, find and remove NaN values in Ratings
   2. Remove duplicates
   3. Get new shape
3. Challenge 3:
   1. Get the 5 highest rates apps
   2. Get the 5 largest apps in terms of size
   3. Get the 5 apps with the most reviews
4. Challenge 4:
   1. Get the count of each content rating into a new dataframe
   2. Create a pie chart with the data and add labels
   3. Create a donut chart
5. Challenge 5:
   1. Analyze the number of installs using `describe()`
   2. Convert the data in the `Installs` column and remove commas
   3. Get count of apps and installs
6. Challenge 6:
   1. Convert the price column to numeric data
   2. Remove all apps that cost more than `$250`
   3. Create a column called "Revenue_Estimate" to hold the value of cost multiplied by installs
   4. Find the top 10 highest grossing apps
7. Chalenge 7:
   1. Get the number of unique rows for paid apps
   2. Find the top 10 categories and the count of apps
   3. Create a bar chart with the results
8. Challenge 8:
   1. Get the count of installs per category
   2. Create a horizontal bar chart with the results
9. Challenge 9:
   1. Create a scatter plot chart showing:
      1. The number of installs in each category
      2. The number of apps in the category
10. Challenge 10:
    1. Find out how many unique genres there are
    2. Find out if there are apps belonging to more than one category
11. Challenge 11:
    1. Using plotly and the genre data:
       1. Create a bar chart
       2. Use a color scale for number of apps in the category
       3. Create a bar chart to compare paid and free apps in each category
       4. Create a box chart to compare downloads between free and paid apps
       5. Create a box plot to show the possible revenue of paid apps in each category
       6. Create a box plot to show the ranges of prices per each category

### Comments

This project took a bit more effort to understand the different charts and graphs along with writing the correct code to manipulate the data with Pandas as it becomes more complex.
