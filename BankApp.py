class Bank:

    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string}\t\tBalance: {self.balance}\n")

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        if amount:
            self.balance -= amount
            self.log_transaction(f"Withdrew ${amount}")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        if amount:
            self.balance += amount
            self.log_transaction(f"Deposited ${amount}")

account = Bank(50.50)

while True:
    try:
        action = input("What kind of action do you want to take? (withdrawal/deposit): ")
    except KeyboardInterrupt:
        print("\nLeaving the ATM\n")
        break

    if action.lower() in ["withdrawal", "deposit"]:
        if action.lower() == "withdrawal":
            amount = input("How much do you want to take out? ")
            account.withdrawal(amount)

        else:
            amount = input("How much do you want to deposit? ")
            account.deposit(amount)

        print("Your balance is", account.balance)
