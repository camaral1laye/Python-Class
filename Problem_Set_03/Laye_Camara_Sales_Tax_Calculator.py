import tax_module  # Import the module containing tax calculations

# Function to display the title
def display_title():
    print("Sales Tax Calculator")
    print()

# Function to get item costs from the user
#print("ENTER ITEMS (ENTER 0 TO END)")
def get_items():
    total = 0
    print("ENTER ITEMS (ENTER 0 TO END)")
    while True:
        cost = float(input("Cost of item: "))
        if cost == 0:
            break
        total += cost
    return total
#print("ENTER ITEMS (ENTER 0 TO END)")
# Main function to handle the program logic
def main():
    display_title()
    
    while True:
        # Get the total cost of items from the user
        total = get_items()
        
        # Calculate sales tax and total after tax using the module
        sales_tax = tax_module.calculate_sales_tax(total)
        total_after_tax = tax_module.calculate_total_after_tax(total)
        
        # Display the results
        print(f"Total:           {total:.2f}")
        print(f"Sales tax:       {sales_tax:.2f}")
        print(f"Total after tax: {total_after_tax:.2f}")
        
        # Ask if the user wants to perform another calculation
        print()
        again = input("Again? (y/n): ").lower()
        print()
        if again != "y":
            #print()
            print("Thanks, bye!")
            break  # Exit the loop if user does not want to continue

# Call the main function to run the program
if __name__ == "__main__":
    main()