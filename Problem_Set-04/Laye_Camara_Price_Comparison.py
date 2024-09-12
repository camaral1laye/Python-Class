#This program calculate price comparison
print("Price Comparison")

price_of_64_oz_size = float(input("Price of 64 oz size: "))
price_of_32_oz_size = float(input("Price of 32 oz size: "))

#calculate price per once
price_per_ounce_64 = price_of_64_oz_size /64
price_per_ouce_32 = price_of_32_oz_size /32

#display
print(f"\nPrice per oz (64 oz): {price_per_ounce_64:.2f}")
print(f"Price per oz (32 oz): {price_per_ouce_32:.2f}")