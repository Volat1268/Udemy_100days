from art import art_text, emoji
from data import MENU, resources


# ------------------------functions------------------------------------------

def check_resources(selected_coffee, stock):
    """ в зависимости от выбранного кофе, определяет, достаточно ли в запасе воды, молока, кофе"""
    result = ""
    if selected_coffee == "espresso":
        if MENU[selected_coffee]["ingredients"]["water"] > stock["water"]:
            result = "Sorry there is not enough water."
            return result
        if MENU[selected_coffee]["ingredients"]["coffee"] > stock["coffee"]:
            result = "Sorry there is not enough coffee."
            return result
        else:
            result = "Please insert coins."
    if selected_coffee == "latte" or selected_coffee == "cappuccino":
        if MENU[selected_coffee]["ingredients"]["water"] > stock["water"]:
            result = "Sorry there is not enough water."
            return result
        if MENU[selected_coffee]["ingredients"]["milk"] > stock["milk"]:
            result = "Sorry there is not enough milk."
            return result
        if MENU[selected_coffee]["ingredients"]["coffee"] > stock["coffee"]:
            result = "Sorry there is not enough coffee."
            return result
        else:
            result = "Please insert coins."
    return result


def payment_for_coffee(selected_coffee):
    """процесс оплаты за выбранный пользователем кофе"""
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    sum_payed = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if sum_payed < MENU[selected_coffee]["cost"]:
        response = "Sorry, that's not enough money. Money refunded."
    elif sum_payed == MENU[selected_coffee]["cost"]:
        response = f"Here is your {selected_coffee} {emoji}. Enjoy!"
    else:
        change = sum_payed - MENU[selected_coffee]["cost"]
        response = f"Here is ${change:.2f} in change.\n" \
                   f"Here is your {selected_coffee} {emoji}. Enjoy!"
    return response


def resources_calculating(selected_coffee, store):
    """вычитание использованных на приготовление кофе ингредиентов"""
    store["money"] += MENU[selected_coffee]["cost"]
    if selected_coffee == "espresso":
        store["water"] -= MENU[selected_coffee]["ingredients"]["water"]
        store["coffee"] -= MENU[selected_coffee]["ingredients"]["coffee"]
    if selected_coffee == "latte" or selected_coffee == "cappuccino":
        store["water"] -= MENU[selected_coffee]["ingredients"]["water"]
        store["coffee"] -= MENU[selected_coffee]["ingredients"]["coffee"]
        store["milk"] -= MENU[selected_coffee]["ingredients"]["milk"]
    return store


def report(distributor):
    print(f"Water: {distributor['water']}ml")
    print(f"Milk: {distributor['milk']}ml")
    print(f"Coffee: {distributor['coffee']}g")
    print(f"Money: ${distributor['money']}")


# ----------------------- variables-----------------------------------------------

resources["money"] = 0
stop_process = False

# ----------------------- programme---------------------------------------------
print(art_text)
while not stop_process:
    user_input = input("  What would you like? (espresso /latte /cappuccino) ").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        type_of_coffee = user_input
        result_check_resources = check_resources(type_of_coffee, resources)
        print(result_check_resources)
        if result_check_resources == "Please insert coins.":
            result_payment_for_coffee = payment_for_coffee(type_of_coffee)
            print(result_payment_for_coffee)
            if result_payment_for_coffee != "Sorry, that's not enough money. Money refunded.":
                resources = resources_calculating(type_of_coffee, resources)
    elif user_input == "report":
        report(resources)
    elif user_input == "off":
        stop_process = True
    else:
        print("Please check you input. Take your choice.")

