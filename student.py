import sqlite3
from tabulate import tabulate

def initialize_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        grade TEXT NOT NULL
                     )''')
    conn.commit()
    conn.close()

def add_student(name, age, grade):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()
    print("Student added successfully!")

def list_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    print(tabulate(students, headers=["ID", "Name", "Age", "Grade"], tablefmt="grid"))

def update_student(student_id, name=None, age=None, grade=None):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE students SET name = ? WHERE id = ?", (name, student_id))
    if age:
        cursor.execute("UPDATE students SET age = ? WHERE id = ?", (age, student_id))
    if grade:
        cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (grade, student_id))
    conn.commit()
    conn.close()
    print("Student updated successfully!")

def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")

def main():
    initialize_db()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. List Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
        elif choice == '2':
            list_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            grade = input("Enter new grade (leave blank to keep current): ")
            update_student(student_id, name or None, int(age) if age else None, grade or None)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
