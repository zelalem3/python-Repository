MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,

        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24

        },
        "cost": 3.0,
    }
}
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def check_resource_sufficent(order_ingredients):
    """checks if the resources are sufficent and returns a type"""
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"there is no enough {item}")
            return False
    return True


def process_coins():
    """calculate the total cost and return the total cost"""
    print("please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?:  ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your ${change} in changes. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that is not enough money, money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


is_on = True
while is_on:
    choice = input("what do you want(espresso/cappuccino/latte): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resource['water']}")
        print(f"milk:{resource['milk']}")
        print(f"coffee:{resource['coffee']}")
    else:
        drink = MENU[choice]
        if check_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
