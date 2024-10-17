# Define the initial inventory
inventory = [
    "wooden staff",
    "wizard hat",
    "cloth shoes"
]

# Maximum number of items the wizard can carry
MAX_ITEMS = 4

def display_menu():
    print("The Wizard Inventory Program\n")
    print("COMMAND MENU")
    print("- show - Show all items")
    print("- grab - Grab an item")
    print("- edit - Edit an item")
    print("- drop - Drop an item")
    print("- exit - Exit program")

def show_items():
    if not inventory:
        print("Your inventory is empty.")
    else:
       # print("Your inventory:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")

def grab_item():
    if len(inventory) >= MAX_ITEMS:
        print("You can't carry any more items. Drop something first.")
        return
    
    item_name = input("Name: ")
    inventory.append(item_name)
    print(f"{item_name} was added.")

def edit_item():
    show_items()
    try:
        item_number = int(input("Number: ")) - 1
        if 0 <= item_number < len(inventory):
            updated_name = input("Updated name: ")
            inventory[item_number] = updated_name
            print(f"Item number {item_number + 1} was updated.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def drop_item():
    show_items()
    try:
        item_number = int(input("Number: ")) - 1
        if 0 <= item_number < len(inventory):
            dropped_item = inventory.pop(item_number)
            print(f"{dropped_item} was dropped.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    display_menu()  # Show the menu once at the start
    while True:
        command = input("\nCommand: ").lower()

        if command == "show":
            show_items()
            # No menu re-display here
        elif command == "grab":
            grab_item()
        elif command == "edit":
            edit_item()
        elif command == "drop":
            drop_item()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()