import random

class User:
    def __init__(self,username,name, password):
        self.username=username
        self.name = name
        self.password = password       
        self.account_number = self.generate_account_number()  
        self.balance = 0.0

    def generate_account_number(self):
        return random.randint(10**15, 10**16 - 1)

    def deposit_amount(self,amount):
        if amount > 0:
            self.balance += amount     
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw_amount(self, amount):
        if self.balance>=amount:
            if amount>0:
                self.balance=self.balance-amount
                print(f'Withdrawn Rs.{amount}. New Balance: {self.balance}')
            else:
                print(f'Amount should be in positive')
        else:
                print(f'Your balance is insufficent')
    
    
    def check_balance(self):
        return self.balance
    

users=[]
def create_user(username,name,password):
    new_users= User(username,name,password)
    users.append(new_users)
    print(f"\nAccount created for {name} with account number: {new_users.account_number}\n")


def login_user(username,password):
    for user in users:
        if user.username == username and user.password==password:
            print(f'\nWelcome {user.name}. Enjoy Using Your Mobile Banking Service\n')
            return user
    print("Invalid username or password.")
    return None


def mobile_banking_services_activate():
    user_full_name=input("Enter your usernane: ").lower()
    user_password=input("Enter your password: ")
    user_detail=login_user(user_full_name, user_password)
    if user_detail is None:
        return 
    while True:
        service=print_mobile_services()
        if service==1:
            amount=float(input(f"Enter the amount to be deposit in your account: "))
            user_detail.deposit_amount(amount)
        elif service ==2:
            amount = float(input("Enter the amount to be withdrawn: "))
            user_detail.withdraw_amount(amount)
        elif service==3:
            print(f'Your balance is {user_detail.check_balance()}')
        elif service==4:
            print('Exiting the Mobile Banking..............\nThank Your for banking with Us..............')
            break
        else:
            print("Invalid choice.")



def print_mobile_services():
    print(f'\n--- Mobile Banking Services ---\n1. Deposit Amount.\n2. Withdraw Amount. \n3. Check balance\n4. Exit\n')
    try:
        choice=int(input("Enter the choice: "))
        return choice
    except ValueError:
        print("\nInvalid Input. Enter the number\n")


def welcome():
    print("\n1. Create Bank Account. \n2. Login for existing user\n")

def start():
    print("Welcome To Bank of Gaurab")
    while True:
        try:
            welcome()
            ch=int(input("Enter the choice: "))
            if ch==1:
                user_full_name=input("Enter your full name: ").title()
                user_username=input("Enter the username").lower()
                user_password=input("Enter your password: ")
                create_user(user_username,user_full_name, user_password)
            elif ch==2:
                mobile_banking_services_activate()
                
            else:
                print("Thank You for banking with us")
        except ValueError:
            print("\nInvalid Input. Enter the number\n")
           
start()
