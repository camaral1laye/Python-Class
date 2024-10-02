# Function to display the title
def display_title():
    print("Hike Calculator")
    print()

# Function to convert miles to feet
def miles_to_feet(miles):
    feet_per_mile = 5280  # 1 mile = 5280 feet
    return int(miles * feet_per_mile)

# Main function to get input and display the result
def main():
    display_title()  # Display the title
    
    # Get the input from the user
    miles = float(input("How many miles did you walk?: "))
    
    # Convert miles to feet
    feet = miles_to_feet(miles)
    
    # Display the result
    print(f"You walked {feet} feet.")

# Call the main function to run the program
main()
