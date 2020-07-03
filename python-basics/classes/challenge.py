# Object Oriented Programming Challenge

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    # deposit
    def deposit(self,amount):
        self.amount = amount
        print('Deposit Accepted')
        return self.balance + self.amount
    
    # withdraw
    def withdraw(self,amount):
        self.amount = amount
        print('Withdrawal Accepted')
        if self.balance - self.amount < 0:
            print('Funds Unavailable!')
        else:
            return self.balance - self.amount


    # account print
    def __str__(self):
        return f'Account owner: {self.owner}\n Account balance: ${self.balance}\n Money for withdraw or deposit ${self.amount}'

# 1. Instantiate the class
acct1 = Account('Jose',100)
acct2 = Account('Ashley', 10)
acct3 = Account('Olivia', 200)

print(acct1.withdraw(75))
print(acct2.deposit(10))
print(acct3.withdraw(210))