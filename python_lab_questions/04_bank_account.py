# Question: Bank account deposit and withdrawal; keep balance at least 1000.
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no, self.balance = account_no, balance
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        else:
            self.balance += amount
            print("Balance:", self.balance)
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive")
        elif self.balance - amount < 1000:
            print("Minimum balance of 1000 must be maintained")
        else:
            self.balance -= amount
            print("Balance:", self.balance)

if __name__ == "__main__":
    account = BankAccount(101, 5000)
    account.deposit(1000)
    account.withdraw(4500)
