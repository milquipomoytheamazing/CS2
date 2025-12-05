# BudgetBuddy: Smart Expense and Savings Tracker

# CS2
Computer science is the study of computers and computational systems. This is the repository of Milqui Pomoy in CS2.

# Overview
BudgetBuddy is a user-friendly tool designed to help individuals track their income, expenses, and savings goals. By providing clear transaction records, visual spending summaries, and progress updates, BudgetBuddy makes money management simple, helping users make informed financial decisions and stay motivated to save.

# Problem Statement
Many young adults overspend because they do not monitor their finances. Without clear tracking, it’s easy to lose sight of spending habits and savings targets. BudgetBuddy solves this problem by giving users an easy and intuitive way to log transactions, understand spending patterns, and reach their financial goals.

# Goals
- Keep track of your money.
- See how you spend your money.
- Save money and monitor progress.
- Know how much you spent each month.

# Features
- Add your income and expenses.
- Sort spending by category (food, school, fun, etc.).
- See how close you are to your savings goal.
- View a chart of your spending.
- Get a monthly summary.

# Inputs
- Amounts of income and expenses.
- Savings goal.

# Outputs
- Simple charts of spending.
- Monthly summary.
- Updates on savings progress.

# Pseudocode
    DISPLAY "Welcome to BudgetBuddy!"
    INPUT user_name
    IF user does not exist THEN
    DISPLAY "Set your savings goal:"
    INPUT savings_goal
    SAVE user profile with savings_goal
    ENDIF

    REPEAT
    DISPLAY "1. Add Income"
    DISPLAY "2. Add Expense"
    DISPLAY "3. View Spending Summary"
    DISPLAY "4. View Savings Progress"
    DISPLAY "5. Generate Monthly Report"
    DISPLAY "6. Exit"
    INPUT user_choice

    SWITCH (user_choice)
        CASE 1:
            INPUT income_amount, income_category, income_date
            ADD income to records
            UPDATE totals and category summaries
        CASE 2:
            INPUT expense_amount, expense_category, expense_date
            ADD expense to records
            UPDATE totals and category summaries
        CASE 3:
            CALCULATE total income and expenses
            GENERATE pie chart by category
            DISPLAY spending summary
        CASE 4:
            CALCULATE savings_progress = total_savings / savings_goal * 100
            DISPLAY "Savings Progress: " + savings_progress + "%"
        CASE 5:
            GENERATE monthly PDF report including totals, category breakdown, and savings progress
            DISPLAY "Report generated successfully!"
        CASE 6:
            DISPLAY "Thank you for using BudgetBuddy!"
            EXIT program
        DEFAULT:
            DISPLAY "Invalid choice. Please try again."
    END SWITCH
    UNTIL user_choice = 6
    END


# Contributors:
Milqui Rouz Pomoy
Liam Josh Dagondon
Rose Julian Lim

Status:
Final proposal completed — ready for development.
