# Day 71 Data Exploration With Pandas

## Overview

For Day 71, we will be exploring the basics of data exploration with Pandas and Jupyter.

### Setup

1. Install [Jupyter](https://pypi.org/project/jupyter/)

### Instructions

1. Import the data from the csv file to a Pandas dataframe
   1. Get the first 5 rows of the table using `head()`
   2. Get the columna and row count of the dataframe using `shape`
   3. Get the column names using `columns`
   4. Get rows with missing data using `isna()`
   5. Get last 5 rows using `tail()`
2. Create a new dataframe from the original
   1. Drop all of the rows with missing data using `dropna()`
   2. Get the last 5 rows from the new dataframe
   3. Access the 'Starting Median Salary' column
      1. Get all rows
      2. Get max value
      3. Get id of max value row
   4. Access the 'Undergraduate Major' column
      1. Get the specific row by using the id from max value row
3. Challenge:
   1. Get the college major with the highest mid-career salary
      1. Print the college major and the salary
   2. Get the college major with the lowest starting salary
      1. Print the college major and the salary
   3. Get the college major with the lowest mid-career salary
      1. Print the college major and the salary
4. Get the difference between 90th percentile and 10th using `subtract()`
   1. Add this to a variable and insert into dataframe using `insert()`
   2. Name the new column 'Spread'
   3. Get the first 5 rows
5. Find the lowest values in Spread
   1. Use `sort_values()`
   2. Get the first 5 college majors and Spread values
6. Challenge:
   1. Find the top 5 degrees with the highest values in the 90th percentile
      1. Print the college major and the salary
   2. Find the degrees with the greatest spread in salaries
      1. Print the college major and the salary
   3. Find majors have the largest difference between high and low earners after graduation
      1. Print the college major and the salary
7. Get the row counts of the 'Group' column
   1. Use `groupby()` and `count()`
8. Get the averages of the 'Group' column
   1. Use `groupby()` and `mean()`

### Comments

This project was simply to explore a new area and did not require more than the data file and to explore some functions in the Pandas library.
