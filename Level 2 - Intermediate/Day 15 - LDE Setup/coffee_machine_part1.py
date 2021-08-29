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
        coin = 0
    else:
        try:  # Check if guess converts to int
            coin = int(coin)  # Try to convert to int
        except ValueError:  # If doesn't convert
            print("\nInvalid entry. Entering 0 for coin count.")
            coin = 0
    return coin


def coffee():
    """Main function for coffee machine."""
    is_on = True

    while is_on:
        drink = input("Would you like an Espresso, Latte, or Cappuccino?\n"
                      "You can press the ENTER key to quit: ").lower()

        coins = {
            "quarters": 0,
            "dimes": 0,
            "nickels": 0,
            "pennies": 0
        }

        if drink == "report":
            print(functions.report("message"))
        elif drink == "off" or drink == "":
            is_on = False
            functions.off()
        else:
            print(f"\nThat will be ${menu.menu[drink]['cost']}")
            print("Please insert payment.\n")

            for coin in coins:
                coins[coin] = input(f"How many {coin}? ")
                coins[coin] = check_input(coins[coin])

            functions.process_transaction(quarters=coins["quarters"],
                                          dimes=coins["dimes"], nickels=coins["nickels"],
                                          pennies=coins["pennies"], drink=drink)


coffee()
