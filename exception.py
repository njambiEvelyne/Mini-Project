try:
    num = int(input("Enter the number: "))

except ValueError:
    print("Invalid Input!")

except Exception as a:
    print(f"Error: {a}")

else:
    print(f"{num} has been input successfully")

finally:
    print("Execution successful!")