import json

try:
    with open('accounts.json', 'r') as file:
        file_content = file.read()
        if file_content:
            accounts = json.loads(file_content)
        else:
            accounts = {}
except FileNotFoundError:
    accounts = {}

def register_def():
    print('Provide your login')
    login = input("Login: ")
    while login in accounts:
        print('Login already exist! Please type another one')
        login = input("Login: ")
    else:
        print('Login successfully created!')
    print('Provide your password')
    password = input("Password: ")
    accounts[login] = password
    with open('accounts.json', 'w') as file:
        json.dump(accounts, file)
        print('Registering successfully! You are already logged in.\nWelcome to calculator!')
        autologin_def(login, password)

def login_def():
    print('Provide your login')
    login = input("Login: ")
    print('Provide your password')
    password = input("Password: ")
    if login in accounts and accounts[login] == password:
        print('Login successfully! \nWelcome to calculator!')
    else:
        print('Error! Please check your login or password and try again')
        print('Provide your login')
        login = input("Login: ")
        print('Provide your password')
        password = input("Password: ")
        if login in accounts and accounts[login] == password:
            print('Login successfully! \nWelcome to calculator!')

def autologin_def(login, password):
    try:
        with open('accounts.json', 'r') as file:
            accounts = json.loads(file_content)
    finally:
        if login in accounts and accounts[login] == password:
            print('Login successfully!\n Welcome to calculator!')

def calculator():
    while True:
        try:
            print('Please select operation by typing number of operation\n'
                  '[1] Addition\n'
                  '[2] Subtraction\n'
                  '[3] Multiplication\n'
                  '[4] Division\n'
                  '[5] EXIT')
            operation = float(input('Number of operation: '))

            if operation == 5:
                print('Thank you! See you again.')
                break

            print('Please provide first number')
            num1 = float(input('Number: '))
            if num1.is_integer():
                num1 = int(num1)

            print('Please provide second number')
            num2 = float(input('Number: '))
            if num2.is_integer():
                num2 = int(num2)

            if operation == 1:
                sum = num1 + num2
                print('Result of addition: ', sum)

            elif operation == 2:
                sub = num1 - num2
                print('Result of subtraction: ', sub)

            elif operation == 3:
                mul = num1 * num2
                print('Result of multiplication: ', mul)

            elif operation == 4:
                div = num1 / num2
                print('Result of division: ', div)

            else:
                print('Error! Please type correct number to select operation.')

        except ValueError:
            print('Error! Please type number only!')
            continue

while True:
    option = input("Type 'register' or 'login': ")
    if option == 'register':
        register_def()
        break
    elif option == 'login':
        login_def()
        break
    else:
        print("Error! Please type only 'register' or 'login'")

calculator()
