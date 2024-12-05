"""

Module name: Inventory.py

Purpose: Holds the list that contains all the “InventoryItem” objects, as well as methods to sort and modify the list

Author: Bobby Cooper, Jacob Norris, Kyle Smith, Matthias Cheeks, Generative AI?

Date: 12/4/2024

"""

from InventoryItem import InventoryItem

class Inventory:
    def __init__(self):
        self.items = []
        self.current_sort = "name"  # Default sorting criteria is by name

    # Method to add an item to the inventory
    def add_item(self, name, price, count):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if count < 0:
            raise ValueError("Count cannot be negative.")
        # Search if the item already exists by name
        existing_item = next((item for item in self.items if item.get_name() == name), None)
        if existing_item:
            try:
                # If the item exists, update its count and price
                existing_item.update_count(count)
                existing_item.update_price(price)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            try:
                # Otherwise, create a new item and add it to the inventory
                new_item = InventoryItem(name, price, count)
                self.items.append(new_item)
            except ValueError as e:
                print(f"Error: {e}")
        self.apply_sort()  # Reapply sorting after modification

    # Method to remove an item by name
    def remove_item(self, name):
        self.items = [item for item in self.items if item.get_name() != name]
        self.apply_sort()  # Reapply sorting after modification

    # Method to find an item by name
    def find_item(self, name):
        return next((item for item in self.items if item.get_name() == name), None)

    # Method to sort inventory by price
    def sort_by_price(self):
        self.items.sort(key=lambda item: item.get_price())
        self.current_sort = "price"

    # Method to sort inventory by count
    def sort_by_count(self):
        self.items.sort(key=lambda item: item.get_count())
        self.current_sort = "count"

    # Method to sort inventory by name (alphabetically)
    def sort_by_name(self):
        self.items.sort(key=lambda item: item.get_name())
        self.current_sort = "name"

    # Apply the current sorting criteria
    def apply_sort(self):
        if self.current_sort == "price":
            self.sort_by_price()
        elif self.current_sort == "count":
            self.sort_by_count()
        else:  # Default to sorting by name
            self.sort_by_name()

    # Display the inventory items
    def display_inventory(self):
        for item in self.items:
            print(f"Name: {item.get_name()}, Price: ${item.get_price():.2f}, Count: {item.get_count()}")
