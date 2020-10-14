class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []

    
    #def add_accout(self, Account):
    #    accounts.append(Account)
    #    print(accounts)

class Account:
    def __init__(self, account_no, amount, Customer):
        self.account_no = account_no
        self.amount = amount
        self.Customer = Customer

class Customer:
    def __init__(self, name):
        self.name = name
    


c1 = Customer('Jens')
c2 = Customer('Erik')
c3 = Customer('Ib')
a1 = Account(1, 100000, c1)
a2 = Account(2, 3000, c2)
a3 = Account(3, 13, c3)
b1 = Bank('Danske Bank') 
b1.accounts.append(a1)
b1.accounts.append(a2)
b1.accounts.append(a3)
print(b1.__dict__)
