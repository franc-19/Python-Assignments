import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited: {amount}. New balance: {self.balance}"
        else:
            return "Invalid deposit amount."
          
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Successfully withdrew: {amount}. New balance: {self.balance}"
        else:
            return "Insufficient balance or invalid amount."
          

    def check_balance(self):
        return f"Current balance: {self.balance}"
    
    def customer_details(self):
        return (f"Customer Name: {self.customer_name}\n"
                f"Account Number: {self.account_number}\n"
                f"Date of Opening: {self.date_of_opening.strftime('%Y-%m-%d')}\n"
                f"Balance: {self.balance}")
     

def get_date_input():
    while True:
        date_input = input("Enter the date of opening (YYYY-MM-DD): ")
        try:
            return datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please try again.")

# Prompt the user for account details
account_number = input("Enter account number: ")
customer_name = input("Enter customer name: ")
date_of_opening = get_date_input()
initial_balance = float(input("Enter initial balance: "))

# Create a BankAccount object using user input
account = BankAccount(account_number, customer_name, date_of_opening, initial_balance)

# Perform some actions interactively
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Customer Details")
    print("5. Exit")
    
    choice = input("Choose an option: ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        print(account.deposit(amount))
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        print(account.withdraw(amount))
    elif choice == '3':
        print(account.check_balance())
    elif choice == '4':
        print(account.customer_details())
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid option. Please choose again.")
