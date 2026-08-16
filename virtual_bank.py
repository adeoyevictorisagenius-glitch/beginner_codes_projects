

class Bank():

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name.title()


    def check_balance(self):
        print(f'Your balance is {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= amount
            print(f'You have withdrawn {amount}. Your new balance is {self.balance}.')

    def deposit(self, amount):
        self.balance += amount
        print(f'You have deposited {amount}. Your new balance is {self.balance}.')

    def transfer(self, amount, recipient):
        if amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= amount
            recipient.balance += amount
            print(f'You have transferred {amount} to {recipient.name}. Your new balance is {self.balance}.')

class User():

    def __init__(self, name):
        self.name = name.title()
        self.balance= 1000

def bank_manager():
    user_name = input('Enter your name: ')
    user= User(name=user_name)
    bank_name = input('Enter the name of your bank: ')
    bank = Bank(user.balance, name=bank_name)

    while True:
        print(f'\nWelcome to {bank_name} Bank! What would you like to do today?')
        print('Enter 1 if you want to check your balance.')
        print('Enter 2 if you want to withdraw money.')
        print('Enter 3 if you want to deposit money.')
        print('Enter 4 if you want to transfer money.')
        choice = input('Enter your choice (1-4) or "exit" to quit: ')
        if choice == '1':
            bank.check_balance()
        elif choice == '2':
            amount = float(input('Enter the amount to withdraw: '))
            bank.withdraw(amount)
        elif choice == '3':
            amount = float(input('Enter the amount to deposit: '))
            bank.deposit(amount)
        elif choice == '4':
            recipient_name = input('Enter the name of the recipient: ')
            user2 =User(name=recipient_name)
            amount = float(input('Enter the amount to transfer: '))
            bank.transfer(amount, user2)
        elif choice.lower() == 'exit':
            print('Thank you for using our banking services!')
            break
        else:
            print('Invalid choice. Please try again.')

bank_manager()