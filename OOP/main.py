from os.path import getsize
from sys import getsizeof


class BankCustomer:
    def __init__(self, name, age, amount, year):
        self.name = name
        self.age = age
        self.amount = amount
        self.year = year

    @classmethod
    def calculation_benefit(cls,amount,year):
        ## each year its amount increases 1.2 %
        amount = 1.2 * amount * year
        return amount

customer1 = BankCustomer("Asliddin", 19, 1000 , 2)
hi = customer1.calculation_benefit(100,5)
print(hi)




