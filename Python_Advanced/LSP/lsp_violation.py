from abc import ABC, abstractmethod
from loguru import logger as log

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, bal:float=0.0):
        self.balance = bal

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

class FixedDepositAccount(BankAccount):
    def __init__(self, bal:float = 0.0):
        self.balance = bal

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self,amount):
        print("Withdrawals are not allowed from Fixed Deposit Accounts until maturity.")

fd = FixedDepositAccount(500.0)
fd.deposit(100)  # This will log a message indicating that withdrawals are not allowed.

    