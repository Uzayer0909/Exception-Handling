try:
    number = int(input("Enter a number:"))
    print(f"You entered {number}")


except ValueError:
    print("The value must be not an integer ")
