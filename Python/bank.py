def show_balance():
    print(f"Your balance is ${balance:.2f}.")

def cash_in():
    amount = float(input("Enter an amount to cash in> "))
    if amount < 0:
        print("That's invalid amount!")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdrawn> "))

    if amount > balance:
        print("You do not have that much in your acocunt!")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0!")
        return 0
    else:
        return amount
balance = 0
Bank_is_online = True

while Bank_is_online:
    print("Welcome to the Tsotne's bank.")
    print("""
1.Show Balance
2.Cash in
3.Withdraw
4.Exit
""")
    
    choice = input("Enter your choice (1-4)> ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += cash_in()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        Bank_is_online = False
    else:
        print("I dont understand that...")

print("Thanks for using our bank!")
print("Have a nice day!")
 