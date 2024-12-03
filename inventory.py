class Inventory: def init(self): self.items = []

# Method to add an item to the inventory
def add_item(self, name, price, count):
    # Search if the item already exists by name
    existing_item = next((item for item in self.items if item.get_name() == name), None)
    if existing_item:
        # If the item exists, update its count and price
        existing_item.update_count(count)
        existing_item.update_price(price)
    else:
        # Otherwise, create a new item and add it to the inventory
        new_item = InventoryItem(name, price, count)
        self.items.append(new_item)

# Method to remove an item by name
def remove_item(self, name):
    self.items = [item for item in self.items if item.get_name() != name]

# Method to find an item by name
def find_item(self, name):
    return next((item for item in self.items if item.get_name() == name), None)

# Method to sort inventory by price
def sort_by_price(self):
    self.items.sort(key=lambda item: item.get_price())

# Method to sort inventory by count
def sort_by_count(self):
    self.items.sort(key=lambda item: item.get_count())

# Method to sort inventory by name (alphabetically)
def sort_by_name(self):
    self.items.sort(key=lambda item: item.get_name())

# Display the inventory items
def display_inventory(self):
    for item in self.items:
        print(f"Name: {item.get_name()}, Price: ${item.get_price():.2f}, Count: {item.get_count()}")

