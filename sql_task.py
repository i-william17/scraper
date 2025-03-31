import sqlite3
from secrets import choice

from tabulate import tabulate

from main import titles


def initialize_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        status TEXT NOT NULL CHECK(status IN ('Pending', 'Completed'))
                     )''')

    conn.commit()
    conn.close()

def add_task(title,description):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, 'Pending')",(title, description))
    conn.commit()
    conn.close()
    print("Task added successfully.")

def list_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    print(tabulate(tasks, headers = ["ID","Title","Description","Status"], tablefmt="grid"))

def update_task(task_id, title=None, description=None, status=None):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    if title:
        cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, task_id))
    if description:
        cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (description, task_id))
    if status:
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))

    conn.commit()
    conn.close()
    print("Task updated successfully.")

def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print("Task deleted successfully.")

def main():
    initialize_db()

    while True:
        print("\nTASK MANAGER")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Tasks")
        print("5. Exit")

        choice = input("Enter choice:")
        if choice == "1":
            title = input("Enter task title:")
            description = input("Enter task description:")
            add_task(title, description)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to update:"))
            title = input("Enter new title(Leave blank to keep current):")
            description = input("Enter new description(Leave blank to keep current):")
            status = input("Enter new status(Pending/Completed, leave blank to keep current):")
            update_task(task_id, title or None, description or None, status or None)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete:"))
            delete_task(task_id)

        elif choice == "5":
            print("EXITING...")
            break

        else:
            print("Invalid choice, please try again...")

if __name__ == "__main__":
    main()

#THE END!!!!!