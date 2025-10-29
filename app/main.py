import json
import os
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = []
    for data in config["customers"]:
        car = Car(
            brand=data["car"]["brand"],
            fuel_consumption=data["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=data["name"],
            location=tuple(data["location"]),
            money=data["money"],
            cart=data["product_cart"],
            car=car
        )
        customers.append(customer)

    shops = [
        Shop(
            name=shop["name"],
            location=tuple(shop["location"]),
            products=shop["products"]
        )
        for shop in config["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs = []
        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to {shop.name} costs {cost}")
            costs.append((cost, shop))

        costs.sort(key=lambda x: x[0])
        for cost, shop in costs:
            if cost <= customer.money:
                print(f"{customer.name} rides to {shop.name}")
                customer.go_to(shop.location)
                shop.print_receipt(customer.name, customer.cart)
                customer.go_home()
                customer.money -= cost
                print(f"{customer.name} rides home")
                print(
                    f"{customer.name} now has {customer.money:.2f} dollars\n"
                )
                break
        else:
            print(
                f"{customer.name} doesn't have enough money to make a "
                "purchase in any shop\n"
            )
