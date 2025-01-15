try:
    no_in_group = int(input("How many are you in the group: "))
    if no_in_group >8:
        print("Hello. I apologise but you'll have to wait for a table.")

    else:
        print("Welcome. Your table is ready!")
except ValueError:
    print("The input must be integers only!")

except Exception as e:
    print(f"Sorry an unexpected error {e} has occurred.")
