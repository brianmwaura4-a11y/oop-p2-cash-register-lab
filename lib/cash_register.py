#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self._discount = 0
        self.total = 0
        self.items = []
        self.previous_transactions = []

        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Add the cost of the items to the total.
        self.total += price * quantity

        # Add each item according to its quantity.
        for _ in range(quantity):
            self.items.append(item)

        # Record the transaction.
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()

        # Remove the transaction's cost from the total.
        self.total -= transaction["price"] * transaction["quantity"]

        # Remove the items from the item list.
        for _ in range(transaction["quantity"]):
            self.items.pop()
  
