print("\nLetter Grade Converter")
print()

#Initialize a variable
continue_program = "y"

while continue_program.lower() == "y":
    grade = int(input("Enter your grade: "))

    if grade >= 88 and grade <= 100:
        print("A")
    elif grade >= 80 and grade <= 87:
        print("B")
    elif grade >= 67 and grade <= 79:
        print("C")
    elif grade >= 60 and grade <= 66:
        print("D")
    else:
        print("F")

# Asking if the user wants to continue
    continue_program = (input("Continue? (y/n): "))
    print()

# Corrected print statement
print("Bye")
