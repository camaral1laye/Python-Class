#This program calculate the coins needed to make change 
# for the specified number of cents
print("\nChange Calculator")
print()
def calculate_change(cents):
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents
    
    return quarters, dimes, nickels, pennies

while True:
    # Get user input for number of cents
    cents = int(input("Enter the number of cents (0-99): "))
    
    # Call the function to calculate the change
    quarters, dimes, nickels, pennies = calculate_change(cents)
    
    # Display the result
    print(f"Quarters: {quarters}")
    print(f"Dimes:    {dimes}")
    print(f"Nickels:  {nickels}")
    print(f"Pennies:  {pennies}")
    
    # Ask if the user wants to continue
    choice = input("Would you like to calculate again? (y/n): ")
    
    # Exit loop if the user chooses not to continue
    if choice.lower() != "y":
        break

print("Goodbye!")
