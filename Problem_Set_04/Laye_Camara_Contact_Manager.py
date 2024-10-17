# Define the initial contact list with sample data
contacts = [
    ["Guido van Rossum", "guido@python.org", "+1 123-456-7890"],
    ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]
]

def display_menu():
    print("Contact Manager")
    print("\nCOMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")

def list_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact[0]}")  # Display only the name

def view_contact():
    try:
        number = int(input("Number: ")) - 1
        if 0 <= number < len(contacts):
            contact = contacts[number]
            print(f"Name: {contact[0]}\nEmail: {contact[1]}\nPhone: {contact[2]}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contacts.append([name, email, phone])
    print(f"{name} was added.")

def delete_contact():
    list_contacts()
    try:
        number = int(input("Number: ")) - 1
        if 0 <= number < len(contacts):
            deleted_contact = contacts.pop(number)
            print(f"{deleted_contact[0]} was deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    display_menu()
    while True:
        command = input("\nCommand: ").lower()

        if command == "list":
            list_contacts()
        elif command == "view":
            list_contacts()  # Show the list of contacts before viewing
            view_contact()
        elif command == "add":
            add_contact()
        elif command == "del":
            delete_contact()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()