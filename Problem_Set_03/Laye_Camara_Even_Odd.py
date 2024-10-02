def check_even_or_odd(number):
    if number % 2 ==0:
        return "even"
    else:
        return "odd"
    
def main():
    print("Even or Odd Checker")

    number = int(input("Enter an integer: "))
    
    result = check_even_or_odd(number)
    
    print(f"This is an {result} number.")
    
if __name__ == "__main__":
    main()