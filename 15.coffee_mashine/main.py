from art import art_text, emoji
from data import MENU, resources


def is_resource_sufficient(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        print()
        return True
    else:
        print("Sorry that's not enough money. Money refunded/")

def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is you {drink_name}")

profit = 0
is_on = True
while is_on:
    choice = input("What do you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

