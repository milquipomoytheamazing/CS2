import json
import os
from datetime import datetime

DATA_FILE = "transactions.json"

# ---------------------------
# File Handling
# ---------------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"transactions": [], "savings_goal": 0}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ---------------------------
# Core Features
# ---------------------------

def add_transaction(data, transaction_type):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "date": date
    }

    data["transactions"].append(transaction)
    save_data(data)
    print("Transaction added successfully!\n")

def set_savings_goal(data):
    goal = float(input("Enter your savings goal: "))
    data["savings_goal"] = goal
    save_data(data)
    print("Savings goal updated!\n")

def calculate_totals(data):
    income = sum(t["amount"] for t in data["transactions"] if t["type"] == "income")
    expenses = sum(t["amount"] for t in data["transactions"] if t["type"] == "expense")
    savings = income - expenses
    return income, expenses, savings

def view_summary(data):
    income, expenses, savings = calculate_totals(data)
    goal = data["savings_goal"]

    print("\n------ Financial Summary ------")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Current Savings: {savings}")
    print(f"Savings Goal: {goal}")

    if goal > 0:
        progress = (savings / goal) * 100
        print(f"Savings Progress: {progress:.2f}%")
    print("--------------------------------\n")

def view_transactions(data):
    if not data["transactions"]:
        print("No transactions recorded.\n")
        return

    print("\n------ Transactions ------")
    for i, t in enumerate(data["transactions"], start=1):
        print(f"{i}. {t['date']} | {t['type']} | {t['category']} | {t['amount']}")
    print("---------------------------\n")

def delete_transaction(data):
    view_transactions(data)
    choice = int(input("Enter transaction number to delete: "))

    if 1 <= choice <= len(data["transactions"]):
        deleted = data["transactions"].pop(choice - 1)
        save_data(data)
        print("Transaction deleted successfully!\n")
    else:
        print("Invalid choice.\n")

# ---------------------------
# Main Menu
# ---------------------------

def main():
    data = load_data()

    while True:
        print("==== BudgetBuddy ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Set Savings Goal")
        print("6. Delete Transaction")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(data, "income")
        elif choice == "2":
            add_transaction(data, "expense")
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            view_summary(data)
        elif choice == "5":
            set_savings_goal(data)
        elif choice == "6":
            delete_transaction(data)
        elif choice == "7":
            print("Thank you for using BudgetBuddy!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
