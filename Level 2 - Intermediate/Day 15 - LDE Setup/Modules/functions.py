from Modules import menu
from os import system, name

resources = menu.resources
resources["money"] = 0


def clear():
    """Function used to clear the console."""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def off():
    """Function used to turn off the coffee machine and end program."""
    return 0


def report(option):
    """Function used to clear the console."""

    if option == "message":
        levels = (f"\nWater Level: {resources['water']}\n"
                  f"Milk Level: {resources['milk']}\n"
                  f"Coffee Level: {resources['coffee']}\n")
        return levels
    elif option == "values":
        return resources


def check_resources(drink):
    """Function used to check if enough resources to make a drink."""
    drink_ingredients = menu.menu[drink]
    levels = report("values")

    for item in drink_ingredients:
        if levels[item] < drink_ingredients["ingredients"][item]:
            print(f"Not enough {item}.")
            return False
    return True


def calculate_payment(quarters, dimes, nickels, pennies, drink):
    """Function used to count total amount of inserted coins and process payment."""
    coin_list = [quarters * .25, dimes * .10, nickels * .05, pennies * .01]
    total_payment = sum(coin_list)

    if total_payment > menu.menu[drink]["cost"]:
        total_refund = total_payment - menu.menu[drink]["cost"]
        resources["money"] += total_payment
        resources["money"] -= total_refund
        print(f"\nHere if your change of ${'{:.2f}'.format(total_refund)}")
        return True
    elif total_payment == menu.menu[drink]["cost"]:
        resources["money"] += total_payment
        return True
    elif total_payment < menu.menu[drink]["cost"]:
        print(f"\nNot enough money. Returning ${'{:.2f}'.format(total_payment)}...\nGoodbye.\n")
        clear()
        return 0


def make_coffee(drink):
    """Function used to make coffee order and update resources."""

    # Update resources
    drink_ingredients = menu.menu[drink]

    if "milk" in drink_ingredients["ingredients"]:
        resources["milk"] -= drink_ingredients["ingredients"]["milk"]
    resources["water"] -= drink_ingredients["ingredients"]["water"]
    resources["coffee"] -= drink_ingredients["ingredients"]["coffee"]

    clear()
    print(f"\nHere is your {drink}! Enjoy!\n")


def process_transaction(quarters=0, dimes=0, nickels=0, pennies=0, drink="latte"):
    """Function used to process and finalize transaction."""

    # Calculate payment
    if calculate_payment(quarters, dimes, nickels, pennies, drink):
        make_coffee(drink)
