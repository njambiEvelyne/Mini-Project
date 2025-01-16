def menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def add_expenses(expenses):
    try:
        amount = int(input("Enter the amount you wish to spend: "))
        category = input("Choose the category eg. Food, Transport: ")
        description = input("Describe the expense(optional) eg. Lunch: ")
        expense = [f"amount:{amount}, category:{category}, description:{description}"]
        expenses.append(expense)
        print("Expense added successfully!")

    except TypeError:
        print("Invalid INPUT! Enter numerical values for amount!")

    except Exception as a:
        print(f"An error: {a}, has occurred!")

def view_expenses(expenses):
    if not expenses:
        print("No expense has been added")

    else:
        print("Recorded Expenses:")
        for index, item in enumerate(expenses, start= 1):
            print(index, item)

def main():
    expenses = []
    while True:
        menu()
        try:
            selection = int(input("Enter your choice: "))
            if selection == 1:
                add_expenses(expenses)
            elif selection == 2:
                view_expenses(expenses)
            elif selection == 3:
                print("Exiting the Expense Tracker. Goodbye!")
                break

        except Exception as e:
            return f"An error {e} has occurred"






main()






