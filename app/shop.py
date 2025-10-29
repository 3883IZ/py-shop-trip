from typing import Dict, List, Tuple
from datetime import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: Tuple[int, int],
        products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, cart: Dict[str, int]) -> float:
        return sum(self.products[p] * q for p, q in cart.items())

    def print_receipt(self, customer_name: str, cart: Dict[str, int]) -> None:
        print(f"\nDate: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0.0
        for product, quantity in cart.items():
            price = self.products[product] * quantity
            print(f"{quantity} {product}s for {price:.0f} dollars")
            total += price
        print(f"Total cost is {total:.2f} dollars")
        print("See you again!\n")
