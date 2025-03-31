import sqlite3
from tabulate import tabulate

def initialize_db():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        type TEXT NOT NULL CHECK(type IN ('Income', 'Expense')),
                        amount REAL NOT NULL,
                        category TEXT NOT NULL,
                        description TEXT,
                        date TEXT NOT NULL
                     )''')
    conn.commit()
    conn.close()

def add_transaction(t_type, amount, category, description, date):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (type, amount, category, description, date) VALUES (?, ?, ?, ?, ?)",
                   (t_type, amount, category, description, date))
    conn.commit()
    conn.close()
    print("Transaction added successfully!")

def list_transactions():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    print(tabulate(transactions, headers=["ID", "Type", "Amount", "Category", "Description", "Date"], tablefmt="grid"))

def get_balance():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'Income'")
    income = cursor.fetchone()[0] or 0
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'Expense'")
    expense = cursor.fetchone()[0] or 0
    conn.close()
    print(f"Total Balance: ${income - expense:.2f} (Income: ${income:.2f}, Expense: ${expense:.2f})")

def delete_transaction(transaction_id):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    print("Transaction deleted successfully!")

def main():
    initialize_db()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Delete Transaction")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            t_type = input("Enter type (Income/Expense): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(t_type, amount, category, description, date)
        elif choice == '2':
            list_transactions()
        elif choice == '3':
            get_balance()
        elif choice == '4':
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete_transaction(transaction_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
