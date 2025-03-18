def show_menu ():
    print("\n--- TO DO LIST MENU ---")
    print("1. View To Do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\n TO DO LIST IS EMPTY")

    else:
        print("\n To Do List:")
        for index,task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("\n Enter the task to add:")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list!")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\n Enter the task number to delete:"))

            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num-1)
                print(f"Task '{removed_task}' deleted!")

            else:
                print("Invalid task number")

        except ValueError:
            print("Please enter a valid number!")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4):")

        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("\nGoodbye! Have a productive day!")
            break
        else:
            print("\nPlease choose a valid number between 1 and 4")

    if __name__ == "__main__":
        main()
