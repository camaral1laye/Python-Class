def display_title():
 print("Prime Number Checker\n")

def get_num():
    while True:
        num = int(input("Please enter an integer between 1 and 5000: "))
        if num < 1 or num > 5000:
            print("Invalid input. Please enter a number between 1 and 5000. Try again.")
        else:
            return num
    
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    if len(factors) == 2:
        print(f"{num} is a prime.")
        print() 
    else:
        print(f"{num} is not a prime")
        print(f"It has a {len(factors)} factors:", end = " ")
        print()
        for factor in factors:
    
            print(factor, end = " ")
        print()
def main():
    display_title()
    choice = "y"
    while choice.lower() == "y":
        num = get_num()
        get_factors(num)
        print()
        choice = input("Try again? (y/n): ")
        print()
    print()
    print("Bye!")

if __name__ == "__main__":
    main()