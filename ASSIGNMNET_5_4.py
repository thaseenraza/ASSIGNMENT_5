class account:                       
    def __init__(self,title = None ,balance = 0):
       self.title = title
       self.balance = balance

class savingsaccount(account):
    def __init__(self,title=None,balance=0,interestrate=0):                 
        super().__init__(title,balance)
        self.interestrate = interestrate

    def savingsaccount_obj(self):
        return f"interestrate : {self.interestrate}"
    def display(self):
        return f"Account(Title , Balance , Interestrate) : Account({self.title},{self.balance} ,{self.interestrate})"
title = str(input("Enter the title : "))
balance = int(input("Enter the balance : "))
interestrate = int(input("Enter the interest rate : "))
  
if __name__ == "__main__":
    savingsaccount = savingsaccount(title,balance,interestrate)
    print(savingsaccount.savingsaccount_obj())
    print(savingsaccount.display())
