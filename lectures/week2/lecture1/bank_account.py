#Real world Scenarios or Problems

#Bank Accounts: Saving Account and Current account inherit from bank account
#Deposit, withdraw, display balance, types of accounts
class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            print("Not enough money")
            return
        self.balance -= amount
        print(f"Withdrawn: Ugx{amount}\n Balance: {self.balance}\n\n")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: Ugx{amount}\n Balance: {self.balance}\n\n")

class CurrentAccount(Account):
    def __init__(self, account_no, balance,interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def AddInterest(self):
        self.balance += (self.balance*self.interest_rate*0.01)
        print(f"Interest: {self.balance*self.interest_rate*0.01}\n Balance: {self.balance}\n\n")

class SavingsAccount(Account):
    def __init__(self, account_no, balance,interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def AddInterest(self):
        self.balance += (self.balance*self.interest_rate*0.01)

#Instantiating the classes
jims_account=CurrentAccount(12345,10000,20)
keyos_account=SavingsAccount(1234512,10000,20)

jims_account.AddInterest()
keyos_account.AddInterest()

jims_account.deposit(10000)
keyos_account.withdraw(1000000)

#Assignment
'''
University System display
'''