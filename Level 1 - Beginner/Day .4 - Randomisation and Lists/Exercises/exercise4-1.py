"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 4
EXERCISE: 4-1 Heads or Tails

INSTRUCTIONS:

    You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

"""

import random

toss = random.randint(0,1)

if toss == 0:
  print("Heads")
elif toss == 1:
  print("Tails")