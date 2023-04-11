class BankAccount:
    balance = 0
    owner = "saswat pandey"

    def withdraw(self, amount):
        if self.balance < amount:
            return f"Dear {self.owner}You cannot withdraw {amount} due to insufficient balance. Your current balance is Rs.{self.balance}."
        else:
            self.balance -= amount
            return f"Dear {self.owner}, you have withdrawn Rs.{amount}. Your current balance is Rs.{self.balance}."

    def deposit(self, amount):
        self.balance += amount
        return f"Dear {self.owner}, you have deposited Rs.{amount}. Your current balance is Rs.{self.balance}."

    def current_balance(self):
        return f"Dear {self.owner}, your total balance is Rs.{self.balance}."


if __name__ == '__main__':
    person1 = BankAccount()

    while True:
        try:
            value = int(input("Choose what you want to do\n1. Withdraw\n2. Deposit\n3. Show current balance\n4. Exit\n"))

            if value == 1:
                amount = int(input("Enter the amount you want to withdraw: "))
                print(person1.withdraw(amount))

            elif value == 2:
                amount = int(input("Enter the amount you want to deposit: "))
                print(person1.deposit(amount))

            elif value == 3:
                print(person1.current_balance())

            elif value == 4:
                print("Thank you for banking with us.")
                break

            else:
                print("Invalid input. Please try again.")

        except ValueError:
            print("Invalid input. Please enter an integer.")

