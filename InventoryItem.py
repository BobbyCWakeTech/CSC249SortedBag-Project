"""

Module name: InventoryItem.py

Purpose: Stores an item and holds attributes of that item such as the item’s name, price, and count, as well as methods to modify these attributes

Author: Bobby Cooper, Jacob Norris, Kyle Smith, Matthias Cheeks, Generative AI?

Date: 12/4/2024

"""

class InventoryItem:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    # Getter methods
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_count(self):
        return self.count

    # Setter methods with validation
    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = price

    def set_count(self, count):
        if count < 0:
            raise ValueError("Count cannot be negative.")
        self.count = count

    # Update methods
    def update_count(self, amount_to_update_by):
        if self.count + amount_to_update_by < 0:
            raise ValueError("Count cannot become negative.")
        self.count += amount_to_update_by

    def update_price(self, amount_to_update_by):
        if self.price + amount_to_update_by < 0:
            raise ValueError("Price cannot become negative.")
        self.price += amount_to_update_by
