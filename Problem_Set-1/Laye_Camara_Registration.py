
#variables initializating
print("Registration Form\n")
firstName = input("First Name: ")
lastName  = input("Last Name: ")
birth_year = input("Birth year: ")

#concat first and last name
full_name = firstName + " " + lastName
temporary_password = firstName + "*"+ birth_year

#Diplay
#print("\nRegistration Form")
print("\nWelcome " +full_name+"!")
print("Your registration is complete.")
print("Your temporary password is: " + firstName +"*"+ birth_year)









