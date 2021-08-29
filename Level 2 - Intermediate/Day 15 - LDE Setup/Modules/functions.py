from Modules import menu
from os import system, name

resources = menu.resources  # Copy menu dictionary
resources["money"] = 0  # Add money key to dictionary


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
    print("\nTurning off...\nGoodbye! 👋")
    return 0    # Ends program


def report(option):
    """Function used to clear the console."""
    if option == "message":     # Gets printed message for console
        levels = (f"\n💧 Water Level: {resources['water']}\n"
                  f"🥛 Milk Level: {resources['milk']}\n"
                  f"☕️ Coffee Level: {resources['coffee']}\n")
        return levels
    elif option == "values":    # Gets values from resources dictionary
        return resources


def check_resources(drink):
    """Function used to check if enough resources to make a drink."""
    drink_ingredients = menu.menu[drink]    # Gets drink ingredients from menu
    levels = report("values")   # Gets current resources values

    for item in drink_ingredients["ingredients"]:  # Run through each ingredient
        if levels[item] < drink_ingredients["ingredients"][item]:   # Check if enough resources for drink
            clear()     # Clears console
            print(f"\nNot enough {item} for a(n) {drink}. Try another selection. 😭\n")    # If not, print message
            return False    # Returns false and returns to drink prompt
    return True     # Returns true and makes drink


def calculate_payment(quarters, dimes, nickels, pennies, drink):
    """Function used to count total amount of inserted coins and process payment."""
    coin_list = [quarters * .25, dimes * .10, nickels * .05, pennies * .01]     # Set total coin values
    total_payment = sum(coin_list)  # Sums the total dollar amount

    if total_payment > menu.menu[drink]["cost"]:    # Checks if user overpaid
        total_refund = total_payment - menu.menu[drink]["cost"]     # Calculate refund amount
        resources["money"] += total_payment     # Add payment amount to money key in resources dictionary
        resources["money"] -= total_refund      # Remove refund amount from money key in resources dictionary
        clear()
        print(f"\nReturning 💲{'{:.2f}'.format(total_refund)} in change... 🤑\n")     # Print refund message
        return True     #
    elif total_payment == menu.menu[drink]["cost"]:     # If payment is exact cost
        resources["money"] += total_payment     # Add payment amount to money key in resources dictionary
        return True     # Continue to make drink
    elif total_payment < menu.menu[drink]["cost"]:  # If payment short
        clear()     # Clear console
        # Tell user not enough money and return the money
        print(f"\nNot enough money. Returning 💲{'{:.2f}'.format(total_payment)}... 😭")
        return 0    # End current loop


def make_coffee(drink):
    """Function used to make coffee order and update resources."""
    # Update resources
    drink_ingredients = menu.menu[drink]    # Copy menu ingredients for drink

    for ingredient in drink_ingredients["ingredients"]:     # Gets ingredients from drink
        resources[ingredient] -= drink_ingredients["ingredients"][ingredient]   # Removes resources to make drink

    print("Dispensing... 🥳")  # Prints dispensing message
    print(f"\nHere is your {drink} ☕️! Enjoy! 👋\n")  # Prints enjoy message


def process_transaction(quarters=0, dimes=0, nickels=0, pennies=0, drink="latte"):
    """Function used to process and finalize transaction."""
    # Check if payment is sufficient
    if calculate_payment(quarters, dimes, nickels, pennies, drink):
        make_coffee(drink)  # Make drink
