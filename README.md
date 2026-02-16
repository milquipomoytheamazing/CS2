# 💰 BudgetBuddy: Smart Expense and Savings Tracker

**CS2 – Computer Science**

BudgetBuddy is a command-line financial tracking application that helps users manage income, expenses, and savings goals. It allows users to record transactions, categorize spending, track savings progress, and view financial summaries.

---

## 📌 Features

* Add income entries
* Add expense entries
* Categorize transactions (Food, School, Transportation, Entertainment, etc.)
* View all recorded transactions
* Delete transactions
* Set and update savings goals
* Automatically calculate total income, expenses, and savings
* View savings progress percentage

---

## 🛠 Technologies Used

* **Python** – Core programming language
* **JSON** – Data storage format for transactions
* **Git & GitHub** – Version control and collaboration

---

## 📂 File Structure

```
BudgetBuddy/
│── budgetbuddy.py
│── transactions.json (auto-generated)
│── README.md
```

* `budgetbuddy.py` → Main program file
* `transactions.json` → Stores income, expenses, and savings goal
* `README.md` → Project documentation

---

## ▶ Installation & How to Run

1. Clone the repository:

   ```
   git clone https://github.com/your-username/BudgetBuddy.git
   ```

2. Navigate into the folder:

   ```
   cd BudgetBuddy
   ```

3. Run the program:

   ```
   python BudgetBuddy.py
   ```

No additional libraries are required.

---

## ⚙ How It Works

1. The program loads stored financial data from a JSON file.

2. Users choose options from a menu (add income, add expense, etc.).

3. The program updates transactions and automatically recalculates totals.

4. Savings progress is computed as:

   ```
   Savings = Total Income − Total Expenses
   Progress (%) = (Savings ÷ Savings Goal) × 100
   ```

5. Data is saved automatically after every update.

---

## 🧠 Key Design Decisions

* JSON was used instead of a database to keep the system simple and beginner-friendly.
* A command-line interface (CLI) was chosen to focus on logic and functionality.
* Data is stored locally to maintain user privacy.

---

## ⚖ Programming and Computing Ethics

This project follows principles from the **Association for Computing Machinery (ACM) Code of Ethics**:

* Respecting intellectual property by writing original code
* Protecting user privacy by storing data locally
* Ensuring transparency in financial calculations
* Designing a simple and accessible user interface

---

## 📊 Current Project Status

✔ Income and expense tracking completed
✔ Savings goal tracking implemented
✔ Transaction deletion feature added
✔ Financial summary calculation working

---

## 👥 Contributors

* Milqui Rouz E. Pomoy
* Liam Josh K. Dagondon
* Rose Julian B. Lim

Just tell me what your teacher prefers 😎
