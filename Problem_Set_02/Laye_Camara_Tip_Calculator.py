#This program calcualate threee option of an appropritate tip 
# after meal at a restaurant
print("\n Tip Calculator")
print()

#Initialize a variable
cost_of_meal = float(input("Cost of meal: "))
print()

#tip percetanges rates
tip_rates_15 = 0.15
tip_rates_20 = 0.20
tip_rates_25 = 0.25

#calculate tips amounts
tip_rates_15 = (round(cost_of_meal * tip_rates_15, 2))
tip_rates_20 = (round(cost_of_meal * tip_rates_20, 2))
tip_rates_25 = (round(cost_of_meal * tip_rates_25, 2))

#total amount of each tip rates
total_amount_15 =(round(tip_rates_15 + cost_of_meal,2))
total_amount_20 = (round(tip_rates_20 + cost_of_meal,2))
total_amount_25 = (round(tip_rates_25 + cost_of_meal,2))

#display the results
print(f"15%\n Tip amount: ${tip_rates_15}")
print(f" Total amount: {total_amount_15}")
print()
print(f"20%\n Tip amount: ${tip_rates_20}")
print(f" Total amount: {total_amount_20}")
print()
print(f"25%\n Tip amount: ${tip_rates_25}")
print(f" Total amount: {total_amount_25}")