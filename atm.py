class ATM:
    def __init__(self, balance=0):
        self.balance=balance

    def check_balance(self):
        print(f"{self.balance} is your account balance")
    def deposit(self,amount):
        if amount >0:
            self.balance += amount
            print(f"{amount} is deposit sucessfully!")
        else:
            print("invalid input")
        self.check_balance()
 
    

    def withdraw(self,amount):
        if 0< amount <= self.balance:
            self.balance -= amount
            print(f"{amount} is withdraw sucessfully")
        elif amount> self.balance:
         print("insuficint balance")
        else:
            print("invalid input")
        self.check_balance()

 
atm=ATM()
 
while True:
    print("1 cheack balance")
    print("2 deposit ")
    print("3 withdraw")

    c=int(input("Enter an operation "))

    if c==1:
       atm.check_balance()
    elif c==2:
        amount=int(input("Enter amount to deposit"))
        atm.deposit(amount)
    elif c==3:
        amount=int(input("Enter amount to withdraw"))
        atm.withdraw(amount)




    


