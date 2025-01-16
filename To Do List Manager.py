def action():
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Exit")

def add_task(tasks):
    """"
    A function to allow the user to add tasks
    """
    task = input("What task do you want to add? ")
    tasks.append(task)
    print(f"{task} has been added successfully")

def view_task(tasks):
    """""
    This method is for the access of the tasks added to the to-do list
    """
    print("Added tasks: ")
    print("Current tasks: ")
    if not tasks:
        print("No tasks have been added.")
    else:
        for index, item in enumerate(tasks, start=1):
            print(f"{index}. {item}")


def mark_complete(tasks):
    """""
    This method allows the user to mark tasks as complete
    """
    if not tasks:
        print("No tasks to complete")
        return
    try:
        view_task(tasks)
        task_index = int(input("Enter the number of the task you completed: "))
        if 1 <= task_index <= len(tasks):
            confirm = input(f"Are you sure you want to mark '{tasks[task_index - 1]}' as complete? (yes/no): ").lower()
            if confirm == "yes":
                completed_task = tasks.pop(task_index - 1)
                print(f'Task "{completed_task}" has been marked as complete.')

        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = []
    while True:
        try:
            action()
            to_do = int(input("Enter the action to perform: "))
            if to_do == 1:
                add_task(tasks)
            elif to_do == 2:
                view_task(tasks)
            elif to_do == 3:
                mark_complete(tasks)
            elif to_do == 4:
                print('''
Exiting the program.
Goodbye!
                            ''')
                break
            else:
                print("Invalid Choice!")


        except ValueError:
            print("Invalid choice. Enter an integer")






        # except ValueError:
        #     print("An error occurred. Enter an integer for to_do")


main()





