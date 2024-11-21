#The user interface for the Create Account program
def get_full_name():
    while True:
        full_name = (input("Enter full name: ")).strip()
        if " " in full_name:  # Check if there's a space separating first and last name
            return full_name
        else:
            print("You must enter your full name.")
def get_password():
    while True:
        password = input("Enter password: ").strip()
        if (len(password) >= 8 and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password)):
            return password
        else:
            print("Password must be at least 8 characters long.")
def main(): 
    full_name = get_full_name()
    first_name = full_name.split()[0]  # Extract first name for greeting
    password = get_password()
    print(f"\nHi {first_name}, thanks for creating an account.")

main()