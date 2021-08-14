"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 1
EXERCISE: 1-4 Variables

INSTRUCTIONS:

    Write a program that switches the values stored in the variables a and b.
    Use the code provided -- do not change the existing code!

    CODE:
        
        a = input("a: ")
        b = input("b: ")

        # WRITE YOUR CODE HERE

        print("a: " + a)
        print("b: " + b)

"""

a = input("a: ")
b = input("b: ")

a,b = b,a

print("a: " + a)
print("b: " + b)