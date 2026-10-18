class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"Deposited {amt}. Balance: {self.balance}")

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amt
            print(f"Withdrawn {amt}. Balance: {self.balance}")

class SavingsAccount(Account):
    def add_interest(self, rate):
        self.balance *= (1 + rate)

if __name__ == "__main__":
    acc = SavingsAccount(input("Owner: "), float(input("Initial balance:")))
    while True:
        c = input("1. Deposit 2. Withdraw 3. Interest 4. Quit: ")
        if c == "1": acc.deposit(float(input("Amount: ")))
        elif c == "2": acc.withdraw(float(input("Amount: ")))
        elif c == "3": acc.add_interest(0.05); print(acc.balance)
        else: break