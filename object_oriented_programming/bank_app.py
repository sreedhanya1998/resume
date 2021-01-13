class Bank:
    def create_account(self,accno,person_name,balance,bank_name):
        self.accno=accno
        self.person_name=person_name
        self.balance=balance
        self.bank_name=bank_name
    def deposit(self,amount):
        self.balance+=amount
        print("your account",self.accno,"has credited with",amount,"has available balance",self.balance)
    def withdraw(self,amount):
        if(amount>self.balance):
            print("you account transaction cancelled")
        else:
            self.balance-=amount
            print("your account",self.accno,"debited with",amount,"your aval balance","self.balance")
    def bal_enq(self):
        print("your account has available balance",self.balance)
obj=Bank()
obj.create_account(1000,"ajay",5000,"SBI")
obj.deposit(5000)
obj.withdraw(5000)
