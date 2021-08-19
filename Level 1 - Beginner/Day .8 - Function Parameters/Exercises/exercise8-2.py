"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 8
EXERCISE: 8-2 Prime Number Checker
LEVEL: Beginner

"""

def prime_checker(number):

    is_prime = True

    # Checks if the number divides by any other 
    # number except 1 and itself
    for i in range(2, number):
        # If number is divided by a number between 2 to input number
        if number % i == 0:
            # Sets prime indicator to False
            is_prime = False
    
    if is_prime:
        # Prints if prime is True
        print("It's a prime number.")
    else:
        # Prints if prime is False
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)