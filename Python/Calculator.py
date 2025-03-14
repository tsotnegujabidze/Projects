# Objective: Make A Calculator


def calculator():
    num1 = float(input('Enter the first number> '))

    num2 = float(input('Enter the second number> '))

    print('''
Please Choose One Of The Following Operations:
1) Add
2) Subtract
3) Multiply
4) Divide
    ''')


    choice = input('Enter your choice> ')

    if choice == '1' or choice.lower() == 'add':
        print(num1 + num2)
    elif choice == '2' or choice.lower() == 'subtract':
        print(num1 - num2)
    elif choice == '3' or choice.lower() == 'multiply':
        print(num1 * num2)
    elif choice == '4' or choice.lower() == 'divide':
        print(num1 / num2)
    else:
        print('Invalid Choice')


print('''Would You Like To Use Our Calculator?
1) Yes
2) No
''')

choice = input('Enter your choice> ')

if choice == '1' or choice.lower() == 'yes':
    calculator()
    print("Thanks For Using Our Calculator!")
elif choice == '2' or choice.lower() == 'no':
    print("Understood, Have A Great Day!")
else:
    print('Invalid Input!')


# Objective Achieved 

