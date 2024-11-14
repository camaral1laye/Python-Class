myNum = None

while not isinstance (myNum, float):
    try:
        myNum = int(input("Enter a number: "))
    except ValueError:
        print("Invalid number. Please try again.")
print("You entered the number:", myNum)

