# CSC249SortedBag-Project
(This doesn't need to look pretty at all because it's not required for the project)

# Description of the selected application and its domain. 

I was thinking along the lines of a Sorted bag of a single kind of object. The object would have attributes for name, price, and amount. Like one object could have the name "jar of pickles" have the price of "$3.00" and have an amount of "50". When you want to update the amount or price of an item, you'd search the bag for an object with a given name then update the attributes of that object once found. The bag could have the objects sorted by price or count of the items, or alphabetized. And to add an object the user would give the name, price and amount and a new object with those attributes would be created then added to the bag. To remove a type of item from the inventory, simply give the name and the program will search them remove that object with that name from the bag. 

Something structured like this: 

Object: Inventory Item 

Attributes: 

Name 

Price 

Count 

Methods: 

updateCount(amountToUpdateBy) 

updatePrice(amountToUpdateBy) 

Standard Getters and Setters 



# Key capabilities and requirements. 

Add Items: Users can add new items to the inventory by specifying the name, price, and count. The application creates a new Inventory Item object and adds it to the sorted bag. 

Update Items: Users can update the price or count of existing items. The program searches for the item by name and modifies its attributes using the updatePrice and updateCount methods.  

Remove Items: Users can remove items from the inventory by providing the item’s name and then the program searches for and deletes the corresponding InventoryItem from the bag. 

Search and Sort: The inventory can be searched by item name. Items can be displayed sorted by price, count, or alphabetically by name 

Scalability: The system should be able to handle a large number of items efficiently, maintaining performance as the inventory grows. 

User Interface: A simple and Intuitive interface for users to interact with in the inventory, possibly through a command-line interface or basic GUI. 
