print("Paycheck Calculator\n")

hours_worked = int(input("Hours Worked: "))
hourly_pay_rate = float(input("Hourly Pay Rate: "))

#gross_pay = input(int())
#tax_rate = input

gross_pay = hours_worked * hourly_pay_rate

tax_rate = float(input("Tax Rate(%): "))
tax_amount = gross_pay*(tax_rate/100)

take_home_pay = gross_pay - tax_amount

print(f"Gross pay: ${gross_pay:.2}")
print(f"Tax Rate: {tax_rate}%")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Take Home Pay: ${take_home_pay:.2f}")