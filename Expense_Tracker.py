"""
Expense Tracker Application

Features:
- Add new expenses
- View all expenses
- Delete an expense by ID
- View total expenses
- Save and load expenses from a JSON file
"""

import json
import os


DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    try:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (eg:- Food, Travel, Bills): ")

        expense_id = len(expenses) + 1
        expense = {
            "id": expense_id,
            "description": description,
            "amount": amount,
            "category": category
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Expense List ---")
    for exp in expenses:
        print(f"ID: {exp['id']} | {exp['description']} | ₹{exp['amount']} | Category: {exp['category']}")
    print("--------------------")

def delete_expense(expenses):
    try:
        expense_id = int(input("Enter the ID of the expense to delete: "))
        updated_expenses = [exp for exp in expenses if exp["id"] != expense_id]

        if len(updated_expenses) == len(expenses):
            print("❌ Expense not found.")
        else:
            save_expenses(updated_expenses)
            print("✅ Expense deleted successfully!")
            expenses[:] = updated_expenses
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")

def view_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expenses: ₹{total}")

def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. View Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            view_total(expenses)
        elif choice == "5":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
