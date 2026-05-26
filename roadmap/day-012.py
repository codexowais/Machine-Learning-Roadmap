# # Day 012 - More OOP: Methods and Encapsulation
#
# Learn: instance methods, simple validation, keeping data and behavior together.
#
# Practice: create a `BankAccount` class with deposit, withdraw, and balance.
#
# Output: a working class that prevents invalid withdrawals.
#
# Review: why can OOP help organize ML projects later?
#

# Code here
class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    balance = 10000

    def show_balance(self):
        print("Your Balance is:", self.balance)

    def Deposit(self,amount):
        self.balance += amount
        print("Deposited :",amount)
        print("Updated Balance is :",self.balance)

    def Withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:    
            self.balance -= amount
            print("Withdrawn :",amount)
            print("Updated Balance is :",self.balance)

account = BankAccount(10000)

while True:                

    
    print ("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")


    choice = int(input("Enter the Operation:"))

    if choice ==1:
        account.show_balance()
    elif choice ==2 :
        amount = int(input("Enter the amount to deposit:"))
        account.Deposit(amount)
    elif choice == 3:
        amount = int(input("Enter the amount to withdraw:"))
        account.Withdraw(amount)
    else:
        print("Thank you")
        break            