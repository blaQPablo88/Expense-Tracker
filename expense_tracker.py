import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.filename = 'expenses.json'
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, description, amount, category, date):
        expense = {
            'description': description,
            'amount': amount,
            'category': category,
            'date': date
        }
        self.expenses.append(expense)
        self.save_expenses()

    def list_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\nExpenses:")
        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. {expense['description']} | Amount: ${expense['amount']} | Category: {expense['category']} | Date: {expense['date']}")

    def total_expenses_by_category(self, category):
        total = sum(expense['amount'] for expense in self.expenses if expense['category'].lower() == category.lower())
        print(f"Total expenses for category '{category}': ${total}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. List Expenses")
        print("3. Total Expenses by Category")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date_str = input("Enter date (YYYY-MM-DD, or leave blank for today): ")
            date = date_str if date_str else datetime.today().strftime('%Y-%m-%d')
            tracker.add_expense(description, amount, category, date)
            print("Expense added successfully.")

        elif choice == '2':
            tracker.list_expenses()

        elif choice == '3':
            category = input("Enter category to view total expenses: ")
            tracker.total_expenses_by_category(category)

        elif choice == '4':
            print("Exiting the expense tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
