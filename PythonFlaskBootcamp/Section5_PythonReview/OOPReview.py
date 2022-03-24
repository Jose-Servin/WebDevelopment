class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"This account belongs to {self.owner} and has a balance of ${self.balance}."

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            return self.balance
        else:
            return "Insufficient Funds."


acct1 = BankAccount('Jose', 100)
print(acct1.deposit(50))
print(acct1.withdraw(50))
print(acct1)
print(acct1.deposit(1000))
print(acct1)
print(acct1.withdraw(1100))
print(acct1)
