def load_sales(filename):
    sales = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                month, amount = line.split()
                sales[month] = float(amount)
    except FileNotFoundError:
        print(f"Error: {filename} not found. A new file will be created.")
    return sales

def save_sales(filename, sales):
    with open(filename, 'w') as file:
        for month, amount in sales.items():
            file.write(f"{month} {amount:.2f}\n")

def view_sales(sales):
    month = input("Three-letter Month: ").lower()
    if month in sales:
        print(f"Sales amount for {month.capitalize()} is {sales[month]:,.2f}.")
    else:
        print("Invalid three-letter month.")

def edit_sales(sales):
    month = input("Three-letter Month: ").lower()
    if month in sales:
        new_amount = float(input("Sales Amount: "))
        sales[month] = new_amount
        print(f"Sales amount for {month.capitalize()} is {sales[month]:,.2f}.")
    else:
        print("Invalid three-letter month.")

def show_totals(sales):
    total = sum(sales.values())
    average = total / len(sales) if sales else 0
    print(f"Yearly total: {total:,.2f}")
    print(f"Monthly average: {average:,.2f}")

def main():
    filename = "monthly_sales.txt"
    sales = load_sales(filename)

    while True:
        command = input("Command: ").lower()
        if command == "view":
            view_sales(sales)
        elif command == "edit":
            edit_sales(sales)
            save_sales(filename, sales)  # Save changes after editing
        elif command == "totals":
            show_totals(sales)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()