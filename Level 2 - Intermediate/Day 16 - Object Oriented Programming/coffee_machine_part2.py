"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 16
PROJECT: Coffee Machine Part 2
LEVEL: Intermediate

"""

import Modules

cash_machine = Modules.MoneyMachine()   # Create object from MoneyMachine class
coffee_machine = Modules.CoffeeMaker()  # Create object from CoffeeMaker class
coffee_menu = Modules.Menu()    # Create object from Menu class


def coffee():
    """Main function for coffee machine."""
    is_on = True    # Boolean for while loop to keep program running

    while is_on:    # While machine is on
        drinks = coffee_menu.get_items()    # Get drink options
        drink_selection = input(f"Would you like an {drinks}?\n"
                                "You can press the ↲ key to quit: ").lower()    # Get order from user

        if drink_selection == "report":   # If user enters report to prompt
            coffee_machine.report()  # Print current resources
            cash_machine.report()  # Print current profit
        elif drink_selection == "off" or drink_selection == "":  # If user enters off or ENTER
            is_on = False   # Stop the loop
            print("\nTurning off...\nGoodbye! 👋")
            return 0     # Turn off machine, end program
        elif drink_selection == "espresso" or drink_selection == "latte" or drink_selection == "cappuccino":

            order = coffee_menu.find_drink(drink_selection)     # Get order information

            # Call function to check if enough resources for drink
            check_ingredients = coffee_machine.is_resource_sufficient(order)

            if check_ingredients:   # If there are enough ingredients
                # Call function to check if enough money for drink
                check_payment = cash_machine.make_payment(order.cost)

            if check_ingredients and check_payment:     # If enough resources and cash payment
                coffee_machine.make_coffee(order)   # Call function to make coffee

        else:
            # Prints error message
            print(f"\nSorry, {drink_selection} is not an option. Please make a valid selection. 🙁\n")


coffee()    # Call initial program
