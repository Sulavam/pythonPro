class ATM:
    def __init__(self, initial_balance, pin):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, pin):
        return self.pin == pin

    def balance_inquiry(self):
        self.transaction_history.append("Balance inquiry")
        return self.balance

    def cash_withdrawal(self, amount):
        if amount > self.balance:
            self.transaction_history.append(f"Failed withdrawal: ${amount}")
            return "Insufficient funds"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            return f"Withdrawal successful. New balance: ${self.balance}"

    def cash_deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        return f"Deposit successful. New balance: ${self.balance}"

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.transaction_history.append("PIN change")
            return "PIN successfully changed"
        else:
            self.transaction_history.append("Failed PIN change attempt")
            return "Incorrect old PIN"

    def get_transaction_history(self):
        return self.transaction_history


# Main function to simulate the ATM operations
def main():
    # Initialize the ATM with a balance and a PIN
    atm = ATM(initial_balance=1000, pin=1234)
    print("Welcome to the ATM Machine Simulation")

    while True:
        print("\nPlease choose an option:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")

        option = input("Enter option: ")

        if option == "1":
            print(f"Your current balance is: ${atm.balance_inquiry()}")

        elif option == "2":
            amount = float(input("Enter amount to withdraw: "))
            print(atm.cash_withdrawal(amount))

        elif option == "3":
            amount = float(input("Enter amount to deposit: "))
            print(atm.cash_deposit(amount))

        elif option == "4":
            old_pin = int(input("Enter old PIN: "))
            new_pin = int(input("Enter new PIN: "))
            print(atm.change_pin(old_pin, new_pin))

        elif option == "5":
            print("Transaction History:")
            for transaction in atm.get_transaction_history():
                print(transaction)

        elif option == "6":
            print("Thank you for using the ATM Machine Simulation. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
