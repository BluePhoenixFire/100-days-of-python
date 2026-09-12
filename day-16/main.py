from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    machine_on = True

    while machine_on:
        user_input = input(f"What would you like? {menu.get_items()}: ").strip().lower()
        if user_input == "off":
            machine_on = False
        elif user_input == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_input)
            if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
