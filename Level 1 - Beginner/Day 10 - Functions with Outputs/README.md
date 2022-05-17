# Day 10 Functions with Outputs

## Overview

Day 10 starts with using dictionaries and lists and learning how to nest them. From there we move into building a Secret Auction appliction.

    Exercise 10.1 - Create a function that takes year and month number and outputs the correct amount of days in the month, keeping note of leap year

The Calculator project is broken up into multiple layers that are added on as we progress. We begin with the basics by developing the functions and flow, to cleaning up the code to shorten and create reusable code.

    Project 10.1 - Build functions for add, subtract, multiply, and divide processes and add code to collect user input for each operation as selected by user
    Project 10.2 - Modify the code to continue looping the program to allow user to continue with previous calculations or start a new calculation

## Project: Calculator

Using what was learned from the project milestones, the final project for Day 10 was to build a completed Calculator program to perform basic functions. The completed program would include importing external modules and cleaning up the code for scalability.

### Instructions

1. Import the logo and print it at the beginning of the program
2. Adjust the code to allow the input of floating or decimal numbers

### Comments

While the purpose of this course was to work with functions that have outputs, I would most likely modify the program a bit more in terms of scalability. As it is right now, it does work. However, I believe it would be worthwhile to combine the functions for `add`, `subtract`, `multiply`, and `divide` and others into one function.

With that function, it would determine the correct process and output the desired results. So, should there be a need to add or remove features, it can simply be adjusted within the function without affecting other parts of the application. And, the function can be used for multiple other purposes instead of just one.

In addition, I added a modulo function to the program to provide a bit extra to the program.

### Replit Demo

[Replit Demo - Calculator](https://replit.com/@EoghyUnscripted/Calculator)
