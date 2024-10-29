def load_sales(filename):
    try:
        with open(filename, 'r') as file:
            sales = [float(line.strip()) for line in file]
        return sales
    except FileNotFoundError:
        return []

def save_sales(filename, sales):
    with open(filename, 'w') as file:
        for sale in sales:
            file.write(f"{sale}\n")

def view_sales(sales):
    for i, sale in enumerate(sales, start=1):
        print(f"Month {i}: {sale:,.2f}")

def edit_sales(sales):
    month = int(input("Enter month number to edit: "))
    if 1 <= month <= len(sales):
        new_sale = float(input("Enter new sales amount: "))
        sales[month - 1] = new_sale
    else:
        print("Invalid month number.")

def show_totals(sales):
    total = sum(sales)
    average = total / len(sales) if sales else 0
    print(f"Total sales: {total:,.2f}")
    print(f"Monthly average: {average:,.2f}")

def add_sales(filename, sales):
    new_sale = float(input("Enter sales amount for the new month: "))
    sales.append(new_sale)
    with open(filename, 'a') as file:
        file.write(f"{new_sale}\n")
    print(f"Added sales for new month: {new_sale:,.2f}")

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
        elif command == "add":
            add_sales(filename, sales)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()