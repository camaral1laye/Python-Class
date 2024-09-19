#This program calculate travel time 
print("Travel Time Calculator")

miles = int(input("Enter miles: "))
per_hour = int(input("Enter miles per hour: "))

# Calculate estimated travel time
hours = miles // per_hour  # Whole number of hours
minutes = (miles % per_hour) * 60 // per_hour  # Remaining minutes

#Estimated travel time
print("\nEstimated travel time:")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")

