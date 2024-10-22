class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.pin = "1234"
        self.transaction_history = []

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")
        self.transaction_history.append("Checked balance")

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        self.transaction_history.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew ₹{amount}")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("Changed PIN")
        else:
            print("Incorrect old PIN.")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    atm = ATM(1000)  # Initial balance of ₹1000
    while True:
        print("\nATM Machine")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "4":
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == "5":
            atm.show_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    