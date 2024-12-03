from Inventory import Inventory
from InventoryItem import InventoryItem

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Find Item")
        print("4. Sort Inventory by Name")
        print("5. Sort Inventory by Price")
        print("6. Sort Inventory by Count")
        print("7. Display Inventory")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                count = int(input("Enter item count: "))
                inventory.add_item(name, price, count)
                print(f"Added {name} to the inventory.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            name = input("Enter item name to remove: ")
            inventory.remove_item(name)
            print(f"Removed {name} from the inventory, if it existed.")

        elif choice == '3':
            name = input("Enter item name to find: ")
            item = inventory.find_item(name)
            if item:
                print(f"Found item - Name: {item.get_name()}, Price: ${item.get_price():.2f}, Count: {item.get_count()}")
            else:
                print("Item not found.")

        elif choice == '4':
            inventory.sort_by_name()
            print("Inventory sorted alphabetically by name.")

        elif choice == '5':
            inventory.sort_by_price()
            print("Inventory sorted by price.")

        elif choice == '6':
            inventory.sort_by_count()
            print("Inventory sorted by count.")

        elif choice == '7':
            print("\nCurrent Inventory:")
            inventory.display_inventory()

        elif choice == '8':
            print("Exiting Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

