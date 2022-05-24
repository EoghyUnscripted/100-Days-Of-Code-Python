# Day 32 SMTPLIB & Datetime

## Overview

For Day 32, we will be moving into more advanced Python to create and send emails on a schedule.

    Exercise 32-1: Motivational Monday Quotes

## Project: Automated Birthday Emailer

Using the provided `letter_#.txt` files and the `birthdays.csv` file, we will create a program that will check if there are birthday's today and send an email wishing them a "Happy birthday!"

### Instructions

1. Fill in some content in the `birthdays.csv` file using the current format
2. Write a function to connect to your email server using SMTP and SSL
3. Write a function that checks the `birthdays.csv` file for birthdays today using `datetime`
   1. If there are none:
      1. Do nothing
   2. If there is one:
      1. Send an email
   3. If there are many:
      1. Loop through the code to send multiple emails
4. Write a function that generates a birthday email
   1. Write code to fill the email contents for email, subject, and body
   2. Write a code that picks a random `letter_#.txt` file as your email body
      1. Replace the `[name]` placeholder with the recipients name
5. Write a function to send the email with the email contents
   1. Send From
   2. Password
   3. Send To
   4. Subject
   5. Message

### Example Input

#### letter_1.txt

    Dear [NAME],

    Happy birthday!

    All the best for the year!

    Eoghy

### Example Output

    Dear John,

    Happy birthday!

    All the best for the year!

    Eoghy

### Comments

For this project, I went a litle beyond what the course materials required. Instead of writing all of the code on a single python file, I chose to break it up into modules to keep it a bit cleaner and less bulky. Ideally, I wanted to make this app as easy as possible for anyone to use.

As an example, the only thing you would need to change is the email and password if you use a google account. However, if you use yahoo, or another email host, you would have to modify the configurations. Otherwise, the program is effective as is and can be scaled.

#### Issues

One drawback is that the way `datetime` is used to match against the records in `birthdays.csv`. For this project, we created a dictionary from a pandas dataframe and set the `{key: value}` pair as `{(month, day): row}`. Which means, we can get the data, but if there are more than one record with the same day and month for birthday, it will only pull one record.

#### Possible Solution

Ideally, what I would have done is created a `{key: value}` pair using `{(email, name): row}`. My reasoning is that emails are unique, but you may have some records with family members or friends that share an email - odd, I know.

Going this route, we can actually loop through the records and match on specific indexes to match the day and month.

This would also allow us to build a new list of today's birthdays with multiple records and we can loop the program to send emails to multiple recipients separately. For example:

      [
         ["John", "John&Jane@email.com"],
         ["Jane", "John&Jane@email.com"]
      ]

That would be everything we need to create our emails. Their name will be used to generate the body and replace the `[NAME]` placeholder in the txt files, and the email will be passed into the SMTPLIB commands.

#### Demo Notes

There is no demo available.
