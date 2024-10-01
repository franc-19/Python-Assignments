# Simple Inventory System

# Initialize an empty dictionary for the inventory
inventory = {}

# Function to add or update items in the inventory
def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"Updated {item_name} with {quantity} more units. Total: {inventory[item_name]} units.")
    else:
        inventory[item_name] = quantity
        print(f"Added {item_name} to the inventory with {quantity} units.")

# Function to retrieve information about a specific item
def get_item(item_name):
    if item_name in inventory:
        print(f"{item_name}: {inventory[item_name]} units available.")
    else:
        print(f"{item_name} is not in the inventory.")

# Function to calculate and display the total quantity of all items in the inventory
def get_total_quantity():
    total_quantity = sum(inventory.values())
    print(f"Total quantity of all items: {total_quantity} units.")

# Main program loop
while True:
    print("\nInventory System Menu:")
    print("1. Add or Update Item")
    print("2. Get Item Information")
    print("3. Get Total Quantity of All Items")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        item_name = input("Enter the item name: ").strip()
        quantity = int(input(f"Enter the quantity for {item_name}: "))
        add_item(item_name, quantity)
    
    elif choice == '2':
        item_name = input("Enter the item name to retrieve: ").strip()
        get_item(item_name)
    
    elif choice == '3':
        get_total_quantity()
    
    elif choice == '4':
        print("Exiting the inventory system.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
