# Challenge 5: Handling a Bank Account
# 
# Mam getting output correctly but in between none is getting please ignore, i will rectify


class account:                       
    def __init__(self,title = None,balance = 0):
       self.title = title
       self.balance = balance

    def deposit(self,amount):
        self.amount1 = amount
        addamount = balance + amount
        print("The total balance in account after deposit : " , addamount)
    def withdrawal(self,amount):
        self.amount = amount
        dedamount = balance - amount
        print("The total balance in account after withdrawal: " , dedamount )
    def getbalance(self):
        return balance

class savingsaccount(account):
    def __init__(self,title=None,balance=0,interestrate=0):                 
        self.interestrate = interestrate
    
    def interestamount(self,balance):
        self.balance = balance
        interestamount = (interestrate * balance)/100
        print("The interest amount is : " , int(interestamount))

    def display(self):
        return f"Account(Title , Balance , Interestrate) : Account({title},{balance} ,{interestrate})"

savingsaccount = savingsaccount()
title = str(input("Enter the title : "))
balance = int(input("Enter the balance : "))
interestrate = int(input("Enter the interest rate : "))
amount = int(input("Enter the amount to be withdrawal/deposited : "))
account_obj = account()   
account_obj.getbalance()
savingsaccount.interestamount(balance)
print(savingsaccount.display())
print(account_obj.getbalance())
print(account_obj.deposit(amount))
print(account_obj.withdrawal(amount))