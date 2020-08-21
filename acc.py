class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    type='checking'

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee


jacks_checking=Checking("jack.txt", 1)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)


jons_checking=Checking("john.txt", 1)
jons_checking.transfer(100)
print(jons_checking.balance)
jons_checking.commit()
print(jons_checking.type)

"""
account=Account("balance.txt")
print(account.balance)
account.deposit(200)
print(account.balance)
account.commit()
"""