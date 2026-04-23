# Simple Bank Account (OOP)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")
    def show_balance(self):
        print(f"Account: {self.owner}, Balance: {self.balance}")

acc = BankAccount(input("Account holder name: "), float(input("Initial deposit: ")))
while True:
    print("\n1. Deposit  2. Withdraw  3. Balance  4. Exit")
    ch = input("Choose: ")
    if ch == '1': acc.deposit(float(input("Amount: ")))
    elif ch == '2': acc.withdraw(float(input("Amount: ")))
    elif ch == '3': acc.show_balance()
    elif ch == '4': break
