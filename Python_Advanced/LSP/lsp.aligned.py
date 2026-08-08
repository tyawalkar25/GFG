from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, bal:float=0.0):
        self.bal = bal

    @abstractmethod
    def deposit(self, amount):
        pass


class WithdrawableBankAccount(BankAccount):
    def __init__(self,bal:float=0.0):
        super().__init__(bal)

    @abstractmethod
    def withdraw(self,amount:float=0.0):
        pass


class SavingsAccount(WithdrawableBankAccount):
    def __init__(self,bal:float=0.0):
        super().__init__(bal)

    def deposit(self,amount:float) -> None:
        self.bal += amount
        print(f"Deposited {amount} and the new balance now is {self.bal}")

    def withdraw(self,amount):
       
        if amount > self.bal:
            print("Insufficient funds for withdrawal.")

        else:
            self.bal -= amount
            print(f"Withdrew {amount} and the new balance now is {self.bal}")

class FixedDepositAccount(BankAccount):
    def __init__(self,bal:float=0.0):
        super().__init__(bal)

    def deposit(self,amount:float) -> None:
        self.bal += amount
        print(f"Deposited {amount} in the fixed deposit and the new balance now is {self.bal}")

fd = FixedDepositAccount(10000.0)
fd.deposit(5000)

sb = SavingsAccount(500.0)
sb.deposit(100)
sb.withdraw(300)
