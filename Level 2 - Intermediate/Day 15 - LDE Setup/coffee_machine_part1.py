"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 15
PROJECT: Coffee Machine Part 1
LEVEL: Intermediate

"""
from Modules import functions, menu


def check_input(coin):
    """Function used to validate inputs."""
    # Converts ENTER on input are converted to 0's
    if coin == "":
        coin = 0    # Set to 0
    else:
        try:  # Check if coin input converts to int
            coin = int(coin)  # Try to convert to int
        except ValueError:  # If doesn't convert
            print("\nInvalid entry. Entering 0 for coin count.")    # Print error message
            coin = 0    # Set to 0
    return coin


def coffee():
    """Main function for coffee machine."""
    is_on = True    # Boolean for while loop to keep program running

    while is_on:    # While machine is on

        user_options = ["espresso", "latte", "cappuccino", "off", "", "report"]
        coins = {
            "quarters": 0,
            "dimes": 0,
            "nickels": 0,
            "pennies": 0
        }   # Set default for coin counts

        drink = input("Would you like an Espresso, Latte, or Cappuccino?\n"
                      "You can press the ↲ key to quit: ").lower()  # Get user drink choice

        if drink in user_options:   # Validates input commands
            if drink == "report":   # If user enters report to prompt
                print(functions.report("message"))  # Print current resources
            elif drink == "off" or drink == "":  # If user enters off or ENTER
                is_on = False   # Stop the loop
                functions.off()     # Turn off machine, end program
            else:
                # Call function to check if enough resources for drink
                if functions.check_resources(drink):
                    print(f"\nThat will be 💲{menu.menu[drink]['cost']}")    # Get price of drink
                    print("Please insert payment:\n")   # Advise to pay

                    for coin in coins:  # Loop through coins dictionary
                        coins[coin] = input(f"How many {coin}? ")   # Get coin count
                        coins[coin] = check_input(coins[coin])  # Check that coin is integer

                    # Call function to process payment
                    functions.process_transaction(quarters=coins["quarters"],
                                                  dimes=coins["dimes"], nickels=coins["nickels"],
                                                  pennies=coins["pennies"], drink=drink)
        else:
            functions.clear()   # Clear console
            print(f"\nSorry, {drink} is not an option. Please make a valid selection. 🙁\n")   # Prints error message

coffee()    # Call initial program
