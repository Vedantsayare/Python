#Build a simple BankAccount class with deposit() and withdraw() methods. Create a custom exception called InsufficientFundsError, and raise it when someone tries to withdraw more than their balance.

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self,amount):
        if amount < 0:
            print("Amount cannot be negative")
        else:
            self.balance += amount
            print(f"Total Balance:{self.balance}")

    def withdraw(self,withdraw_amount):
        if withdraw_amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds!")
        else:
            print("Amount withdrawn successfully!")
            self.balance -= withdraw_amount
            print(f"Balance remaining: {self.balance}")
            
        
account = BankAccount()
account.deposit(400)
try:
    account.withdraw(300)
except InsufficientFundsError as e:
    print(e)
