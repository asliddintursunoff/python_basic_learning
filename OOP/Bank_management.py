class Account:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self , amount):
        self.balance += amount
        return self.balance
    def balanced(self):
        return self.balance
class CheckingAccount(Account):
    overdraft_limit = 30_000
    def __init__(self, account_holder, account_number, balance, amount):
        super().__init__(account_holder, account_number, balance)
        self.amount = amount

    def withdraw(self):
        if Account.balanced(self) >= self.overdraft_limit:
            self.balance = self.balance - self.amount
            print(f"You withdraw {self.amount}\nYou have {self.balance}.")
            return self.balance
        else:
            return f"Minimum withdraw amount is {self.overdraft_limit}"

    def balan(self):
        return self.balance
obj = Account("asliddin", 9823232323, 100_000)

obj1 = CheckingAccount("asliddin", 9823232323, 100_000,30_000)
print(obj1.balanced())

print(obj1.withdraw())
print(obj1.balan())
print(obj1.balanced())
