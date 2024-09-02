class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, user_id, password):
        if user_id in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[user_id] = {'password': password, 'balance': 0}
            print("Thank You! Your account has been created!")

    def login(self, user_id, password):
        if user_id in self.accounts and self.accounts[user_id]['password'] == password:
            print("Access Granted!")
            return True
        else:
            print("*** LOGIN FAILED! ***")
            return False

    def deposit(self, user_id, amount):
        self.accounts[user_id]['balance'] += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self, user_id, amount):
        if self.accounts[user_id]['balance'] >= amount:
            self.accounts[user_id]['balance'] -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def request_balance(self, user_id):
        balance = self.accounts[user_id]['balance']
        print(f"Your balance is ${balance:.2f}.")

def main():
    atm = ATM()

    while True:
        print("Please select an option from the menu below:")
        print("l -> Login")
        print("c -> Create New Account")
        print("q -> Quit")

        choice = input("> ").lower()

        if choice == 'c':
            user_id = input("Please enter your user name: ")
            password = input("Please enter your password: ")
            atm.create_account(user_id, password)

        elif choice == 'l':
            user_id = input("Please enter your user id: ")
            password = input("Please enter your password: ")

            if atm.login(user_id, password):
                while True:
                    print("\nd -> Deposit Money")
                    print("w -> Withdraw Money")
                    print("r -> Request Balance")
                    print("q -> Quit")

                    action = input("> ").lower()

                    if action == 'd':
                        amount = float(input("Amount of deposit: $"))
                        atm.deposit(user_id, amount)

                    elif action == 'w':
                        amount = float(input("Amount of withdrawal: $"))
                        atm.withdraw(user_id, amount)

                    elif action == 'r':
                        atm.request_balance(user_id)

                    elif action == 'q':
                        break

                    else:
                        print("Invalid option, please try again.")
            
        elif choice == 'q':
            print("Thank you for using the ATM Machine. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
