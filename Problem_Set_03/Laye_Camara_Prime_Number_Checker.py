# Function to check if the number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to count factors of a number
def count_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return len(factors), factors

# Function to get a valid integer from user between 1 and 5000
def get_valid_integer():
    while True:
        try:
            number = int(input("Please enter an integer between 1 and 5000: "))
            if 1 <= number <= 5000:
                return number
            else:
                print("Invalid integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Main function to control the program
def main():
    print("Prime Number Checker")
    print()
    
    while True:
        # Get valid input from user
        number = get_valid_integer()

        # Check if the number is prime
        if is_prime(number):
            print("Invalid interger. Please try again")
        else:
            # Count factors if the number is not prime
            factor_count, factors = count_factors(number)
            print(f"{number} is a prime number.")
            print(f"It has {factor_count} factors: {factors}")

        # Ask if user wants to try again
        again = input("Try again? (y/n): ").lower()
        if again != 'y':
            print("Bye!")
            break

# Entry point of the program
if __name__ == "__main__":
    main()