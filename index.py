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
        else:
            print("Deposit amount must be positive.")
    
    def withdraw_amount(self, amount):
        if self.balance>=amount:
            if amount>0:
                self.balance=self.balance-amount
            else:
                print(f'Amount should be in positive')
        else:
                print(f'Your balance is insufficent')
    
    
    def check_balance(self):
        return self.balance
    
    def check_requirement(self,amount):
        if amount>0:
            if self.balance>=amount:
                return True
            else:
                print(f'\n Insufficent Balance. \n')
        else:
            print(f'\n Amount must be positive. \n')

        return False
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

def find_user(account_no):
    for user in users:
        if user.account_number == account_no:
            return user
    return None


def mobile_banking_services_activate():
    user_full_name=input("Enter your usernane: ").lower()
    user_password=input("Enter your password: ")
    user_detail=login_user(user_full_name, user_password)
    if user_detail is None:
        print(f'No User found') 
        return
    while True:
        service=print_mobile_services()
        if service==1:
            amount=float(input(f"Enter the amount to be deposit in your account: "))
            user_detail.deposit_amount(amount)
            print(f'\nYour account {user_detail.account_number} has been credited to Rs. {amount}')
        elif service ==2:
            amount = float(input("Enter the amount to be withdrawn: "))
            user_detail.withdraw_amount(amount)
            print(f'\nYour account {user_detail.account_number} has been debited by Rs. {amount}')

        elif service==3:
            print(f'Your balance is {user_detail.check_balance()}')
        
        elif service==4:
            fund_transfer_acc=int(input("Enter the receiver account number: "))
            full_name=input("Ente the receiver name: ").title()
            amount=int(input("Enter the amount: "))
            if user_detail.check_requirement(amount):
                transfer_acc=find_user(fund_transfer_acc)
                if transfer_acc is None:
                    print("Account Number not found.")
                    continue
                else:
                    if transfer_acc.name == full_name:
                        transfer_acc.deposit_amount(amount)
                        user_detail.withdraw_amount(amount)
                        print(f'Rs. {amount} has been transfered to {transfer_acc.account_number} number from {user_detail.account_number}. Remarks: {user_detail.name} to {transfer_acc.name}')
                        print(f'Your new balance is {user_detail.check_balance()} ')
                    else:
                        print(f'Account with {full_name} didnt match')
                

        elif service==5:
            print('Exiting the Mobile Banking..............\nThank Your for banking with Us..............')
            break
        else:
            print("Invalid choice.")

       

def print_mobile_services():
    print(f'\n--- Mobile Banking Services ---\n1. Deposit Amount.\n2. Withdraw Amount. \n3. Check balance\n4. Fund transfer\n5. Exit\n')
    try:
        choice=int(input("Enter the choice: "))
        return choice
    except ValueError:
        print("\nInvalid Input. Enter the number\n")


def welcome():
    print("\n1. Create Bank Account. \n2. Login for existing user\n3. Exit\n")

def start():
    print("Welcome To Bank of Gaurab")
    while True:
        try:
            welcome()
            ch=int(input("Enter the choice: "))
            if ch==1:
                user_full_name=input("Enter your full name: ").title()
                user_username=input("Enter the username: ").lower()
                user_password=input("Enter your password: ")
                if any(acc_user.username == user_username for acc_user in users):
                    print("Account with this username already exists. Please try a different username.\n")
                    continue  
                create_user(user_username,user_full_name, user_password)
            elif ch==2:
                mobile_banking_services_activate()
            
            else:
                print("Thank You for banking with us")
                break

        except ValueError:
            print("\nInvalid Input. Enter the number\n")
           
start()
