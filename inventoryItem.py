class InventoryItem: def init(self, name, price, count): self.name = name self.price = price self.count = count

# Getter methods
def get_name(self):
    return self.name

def get_price(self):
    return self.price

def get_count(self):
    return self.count

# Setter methods
def set_name(self, name):
    self.name = name

def set_price(self, price):
    self.price = price

def set_count(self, count):
    self.count = count

# Update methods
def update_count(self, amount_to_update_by):
    self.count += amount_to_update_by

def update_price(self, amount_to_update_by):
    self.price += amount_to_update_by
