class BankAccount:
    balance=0
    owner="utshav Adhikari"
    def WithDrwal(self,WithdrawlAmount):
        self.amount=WithdrawlAmount
        if self.balance < self.amount:
            return("you cannot withdraw the amount")
        else:
            self.balance=self.balance-self.amount
            return (f"Dear {self.owner}, \n you have withdraw amount RS.{self.amount} Now, your current balace is RS.{self.balance}")
    def Deposit(self,DepositAmount):
        self.amount=DepositAmount
        self.balance = self.balance + self.amount
        return (f"Dear {self.owner}, \nYou have deposited RS.{self.amount} Now, your current balance is RS.{self.balance} ")
    def Current_balance(self):
        return(f"Dear {self.owner}, \nYour total balance is RS.{self.balance}")

if __name__ == '__main__':
    person1=BankAccount()
    
    print(person1.Deposit(1000))
    print(person1.WithDrwal(500))
    print(person1.Deposit(39))
    print(person1.Current_balance())
