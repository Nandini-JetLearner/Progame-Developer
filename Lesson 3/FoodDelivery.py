# Encapsulation - managing order details securely
# Abstraction- defining a payment system
# Polymorphism-different payment methods behaving differently

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

#Encapsulation
class Order:
    def __init__(self,item,price):
        self.__item= item
        self.__price= price

    def get_order_details(self):
        return f"Item: {self.__item}, Price {self.__price} dollars"
    
    def get_price(self):
        return self.__price
    
 #Polymorphism
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class UpiPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using UPI"

class CashPayment(Payment):
    def pay(self,amount):
        return f"Paid {amount} using cash"


order1=Order("Burger", 13)
print(order1.get_order_details())

payments=[CreditCardPayment(),UpiPayment(),CashPayment()]

for method in payments:
    print(method.pay(order1.get_price()))