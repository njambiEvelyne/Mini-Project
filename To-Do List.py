def choice():
    print("\n\t\t\t\tTO-DO LIST TOOL\n")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")

def main():
    to_do_list = []
    while True:
        choice()
        task_action = input("Enter the action to perform: ")

        if task_action == "1":
            task = input("Enter the task: ")
            to_do_list.append(task)
            print(f"{task} has been added to the list.")

        elif task_action == "2":
            task = input("Enter the task to be removed: ")
            if task in to_do_list:
                to_do_list.remove(task)
                print(f"{task} has been removed from the list")
            else:
                print(f"{task} is not included in the list")

        elif task_action == "3":
            if to_do_list:
                print("Your tasks to perform")
                for i, task in enumerate(to_do_list, start=1):
                    print(f"{i}. {task}")
            else:
                print("Your list is empty")

        elif task_action =="4":
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")






main()
