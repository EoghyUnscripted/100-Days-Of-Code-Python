"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 2
EXERCISE: 2-1 Data Types
LEVEL: Beginner

INSTRUCTIONS:

    Write a program that adds the digits in a 2 digit number. 
    e.g. if the input was 35, then the output should be 3 + 5 = 8

    Use the code provided -- do not change the existing code!

    CODE:

        two_digit_number = input("Type a two digit number: ")

        # WRITE YOUR CODE HERE

"""

two_digit_number = input("Type a two digit number: ")

if len(two_digit_number) > 2:
  print("That is not a two digit number.\nTry, again.")
  exit

if len(two_digit_number) == 2:
  
  i = 0
  num = 0

  while i < 2:

    num = num + int(two_digit_number[i])
    i += 1
      
  print(num)