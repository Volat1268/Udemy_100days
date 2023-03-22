from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()



is_on = True
while is_on:
    menu_choice = menu.get_items()
    drink = input(f"What would you like? ({menu_choice}): ")
    if drink == "off":
        is_on = False
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
        is_on = False
    else:
        drink_ordered = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(drink_ordered) and money_machine.make_payment(drink_ordered.cost):
            coffee_maker.make_coffee(drink_ordered)
