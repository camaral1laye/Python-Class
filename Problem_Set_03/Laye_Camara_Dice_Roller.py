import random

# Function to roll a single die
def roll_die():
    return random.randint(1, 6)

# Function to display the title
def display_title():
    print("Dice Roller")
    print()

# Function to roll two dice and check for special messages
def roll_dice():
    die1 = roll_die()  # Roll the first die
    die2 = roll_die()  # Roll the second die
    total = die1 + die2
    
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

    # Check for special messages
    if die1 == 1 and die2 == 1:
        print("Snake eyes!")  # Both dice are 1
    elif die1 == 6 and die2 == 6:
        print("Boxcars!")  # Both dice are 6

def main():
    display_title()
    
    while True:
        roll = input("Roll the dice? (y/n): ").lower()
        if roll != 'y':
            break  # Exit if the user doesn't want to roll the dice

        # Roll the dice and display the result
        roll_dice()
        
        print()  # Blank line for readability

    print("Thanks for playing!")

# Entry point of the program
if __name__ == "__main__":
    main()