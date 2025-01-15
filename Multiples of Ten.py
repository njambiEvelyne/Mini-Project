try:
    num = int(input("Enter a number to determine whether it is a multiple of 10: "))
    if num % 10 == 0:
        print(f"The number {num} is a multiple of 10.")
    else:
        print(f"Number: {num} is not a multiple of 10.")

except ValueError:
    print("Must be a numeric value!")

except Exception as a:
    print(f"Oops! An error: {a} has occurred")