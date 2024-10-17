def get_sales():
    sales = []
    for i in range(1, 5):
        while True:
            try:
                sale = float(input(f"Enter sales for Q{i}: "))
                sales.append(round(sale, 2))  # Round to 2 decimal places
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return sales

def calculate_totals(sales):
    total = round(sum(sales), 2)
    average = round(total / len(sales), 2)
    lowest = min(sales)
    highest = max(sales)
    return total, average, lowest, highest

def display_results(total, average, lowest, highest):
    print(f"\nTotal: {total}")
    print(f"Average Quarter: {average}")
    print(f"Lowest Quarter: {lowest}")
    print(f"Highest Quarter: {highest}")

def main():
    print("The Quarterly Sales Program\n")
    
    sales = get_sales()
    total, average, lowest, highest = calculate_totals(sales)
    
    display_results(total, average, lowest, highest)

if __name__ == "__main__":
    main()