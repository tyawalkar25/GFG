# Demonstrates the Open/Closed Principle using an abstract PaymentMethod base class
# and concrete payment strategies like UPI, CreditCard, DebitCard, and NetBanking.
# PaymentProcessor accepts any PaymentMethod implementation and processes payments
# without needing to change when new payment methods are added.
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Debit Card.")

class NetBanking(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking.")

class Wallet(PaymentMethod):
    def pay(self,amount):
        print(f"Paid {amount} using my wallet")



#pm = PaymentMethod()  # This will raise an error because PaymentMethod is an abstract class and cannot be instantiated directly.

class PaymentProcessor:

    def __init__(self, payment_method : PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: float):
        self.payment_method.pay(amount)

nb = NetBanking()
my_wallet = Wallet()

xyz = PaymentProcessor(my_wallet)
xyz.process_payment(1000)