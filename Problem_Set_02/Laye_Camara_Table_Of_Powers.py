#This program displays a table of squares and 
#cubes for the specified ranges of numbers
print("\nTable of Powers\n")

# Function to display the table of squares and cubes
def display_table(start, stop):
    """Displays a table of squares and cubes from start to stop."""
    print("\nNumber\tSquared\tCubed")
    print("=" *5+"  "+"="*5+"   "+"="*5)

    for x in range(start, stop + 1):
        square = x ** 2
        cube = x ** 3
        print(f"{x}\t{square}\t{cube}")

# Main program loop
while True:
    try:
        # Prompt the user for start and stop integers
        start = int(input("Start number: "))
        stop = int(input("Stop number: "))

        # Ensure the start is less than the stop integer
        if start > stop:
            print("Error: The start integer must be less than the stop integer. Please try again.")
        else:
            # Display the table of squares and cubes
            display_table(start, stop)
            
            # Asking if the user wants to continue
            choice = input("Would you like to enter another range? (y/n): ").strip().lower()
            if choice != "y":
                break
    except ValueError:
        # Handle invalid input
        print("Error: You must enter valid integers. Please try again.")

# Goodbye message
print("Thank you for using the program!")