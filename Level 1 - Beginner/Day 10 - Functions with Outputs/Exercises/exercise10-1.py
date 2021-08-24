"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 10
EXERCISE: 10-1 Days in a Month
LEVEL: Beginner

"""

def is_leap(year):  # Checks if entered year is a leap year

    # Checks if year divides by 4
    if year % 4 == 0:
        # Checks if year also divides by 100
        if year % 100 == 0:
            # Checks if year also divides by 400
            if year % 400 == 0:
                return True
            # If does not also divide by 400
            else:
                return False
        # If year does not also divide by 100
        else:
            return True
    # If year does not divide by 4
    else:
        return False

def days_in_month(year, month): # Gets the input and outputs the days in month
    # List of day counts in each month
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):   # Calls leap year checker
        month_days[1] = 29  # If leap year is True, sets Feb days to 29
        return month_days[month - 1]    # Returns the output with updated days

    return month_days[month - 1]    # Returns the number of days

year = int(input("Enter a year: ")) # Gets user input for year
month = int(input("Enter a month: "))   # Gets user input for month
days = days_in_month(year, month)   # Calls function to get days count, sets to variable
print(days) # Outputs result to user
