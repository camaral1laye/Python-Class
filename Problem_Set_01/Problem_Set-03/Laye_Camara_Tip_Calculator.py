#This program calculate tip and total for a meal at the restaurant 
print("Tip Calculator\n")

cost_of_meal = float(input("Cost of meal: "))
tip_percent = float(input("Tip percent: "))

#calculating the tip amount
tip = cost_of_meal*(tip_percent/100)
total_amount = cost_of_meal +tip

#display
print(f"Tip amount: {tip:.2f}")
print(f"Total amount: ${total_amount:.2f}")



#print(f"Gross pay: ${gross_pay:.2}")