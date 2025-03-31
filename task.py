import json
import os
from secrets import choice

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task."""
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {
        "name": task_name,
        "description": task_description,
        "completed": False
    }
    save_tasks(tasks)
    print(f"Task '{task_name}' added with ID {task_id}.")

def view_tasks(tasks):
    """ View all tasks """
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            status = ("Completed" if task["completed"] else "Not Completed")
            print(f"ID: {task_id}, Name: {task['name']}, Description:{task['description']}, Status: {status}")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    task_id = input("Enter the task ID to mark as completed: ")
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_id]['name']}' marked as completed.")
    else:
        print("Task ID not found.")

def delete_task(tasks):
    """ Delete task"""
    task_id = input("Enter the task ID to delete:")
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Tasks '{deleted_task['name']}' deleted.")
    else:
        print(f"Task ID not found.")

def main():
    """Main function for task manager"""
    task = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your Choice:")

        if choice == "1":
            add_task(task)
        elif choice == "2":
            view_tasks(task)
        elif choice == "3":
            mark_task_completed(task)
        elif choice == "4":
            delete_task(task)
        elif choice == "5":
            print("Exiting Task manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()

