from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
cash = MoneyMachine()

power_on = True
while power_on:

    choice = input(f"What would you like?  ({menu.get_items()})  ").lower()

    if choice == "off":
        power_on = False
    elif choice == "report":
        maker.report()
        cash.report()
    else:
        choice = menu.find_drink(choice)
        if maker.is_resource_sufficient(choice) and cash.make_payment(choice.cost):
            maker.make_coffee(choice)
