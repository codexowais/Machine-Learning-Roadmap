# # Day 015 - Python Review Project
#
# Learn: consolidate core Python.
#
# Practice: build a mini expense tracker using dictionaries, files, and functions.
#
# Output: add expenses, show total, show category totals, save/load data.
#
# Review: are you comfortable writing a 100-line Python script?
#

# Code here

expenses = [
    {
    "category":"food",
    "amount":500
},

{
    "category":"transport",
    "amount":1000
},
{

    "category":"internet",
    "amount":349
}

]

def add_expense():
    category = input("Select the category: ")
    amount = int(input("Enter the amount: "))

    expense = {
        "category":category,
        "amount": amount
    }

    expenses.append(expense)

    print("\nExpense Added Successfully")
    print(expense)