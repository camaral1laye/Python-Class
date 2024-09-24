# This program compares the total cost of an order including shipping
print("=" * 100)
print("Shipping Calculator")
print("=" * 100)

# Function to calculate shipping cost
def calculate_shipping_cost(order_total):
    """Function to calculate shipping cost based on order total."""
    if order_total < 30.00:
        return 5.95
    elif 30.00 <= order_total <= 49.99:
        return 7.95
    elif 50.00 <= order_total <= 74.99:
        return 9.95
    else:
        return 0.00  # Free shipping for orders >= 75.00

while True:
    try:
        # Get user input for the order total
        order_total = float(input("Cost of items ordered: "))

        # If the user enters a negative number, display an error
        if order_total < 0:
            print("You must enter a valid number. Please try again.")
        else:
            # Calculate the shipping cost
            shipping_cost = calculate_shipping_cost(order_total)

            # Calculate the final total including shipping
            final_total = order_total + shipping_cost

            # Display the results
            print(f"Shipping Cost:         ${shipping_cost:.2f}")
            print(f"Total Cost:            ${final_total:.2f}")
            
            # Asking if the user wants to continue
            print()
            choice = input("Continue? (y/n): ").strip().lower()

            # Break loop if the user doesn't want to continue
            if choice != "y":
                break
    except ValueError:
        # Handle invalid input (e.g., non-numeric values)
        print("You must enter a valid number. Please try again.")

# Goodbye message after exiting the loop
print("="*100)
print("Bye!")