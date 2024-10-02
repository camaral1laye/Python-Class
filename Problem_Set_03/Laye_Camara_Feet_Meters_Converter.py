# Conversion functions in a separate module
def feet_to_meters(feet):
    """Converts feet to meters."""
    return round(feet * 0.3048, 2)

def meters_to_feet(meters):
    """Converts meters to feet."""
    return round(meters / 0.3048, 2)

# Display title function
def display_title():
    print("Feet and Meters Converter")
    print()

# Display menu function
def display_menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

# Main function for input and conversion handling
def main():
    display_title()  # Display the title once
    
    while True:
        display_menu()  # Show the conversion menu
        
        # Get user selection
        choice = input("Select a conversion (a/b): ").lower()
        print()
        if choice == "a":  # Feet to meters conversion
            feet = float(input("Enter feet: "))
            meters = feet_to_meters(feet)
            print(f"{meters} meters.")
            
        elif choice == "b":  # Meters to feet conversion
            meters = float(input("Enter meters: "))
            feet = meters_to_feet(meters)
            print(f"{meters} meters is {feet} feet.")
            
        else:
            print("Invalid choice. Please select 'a' or 'b'.")
            continue
        
        # Ask user if they want to perform another conversion
        print()
        again = input("Would you like to perform another conversion? (y/n): ").lower()
        print()
        if again != "y":
            print("Thanks, bye!")
            break  # Exit the loop if user does not want to continue

# Call the main function to start the program
main()