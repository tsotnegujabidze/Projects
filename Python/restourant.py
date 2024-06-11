menu = {
    'pizza': 10,
    'burger': 8,
    'salad': 6,
    'pasta': 12,
    'soda': 2
}

print("Welcome to Los Pollos Hermanos!")
print("Menu:")
for item, price in menu.items():
    print(item, "-", price)

order = {}
print("\nWhat would you like to order? (Enter 'done' to finish)")
while True:
    item = input("Enter item: ").strip().lower()
    if item == 'done':
        break
    elif item in menu:
        quantity = int(input("Enter quantity: "))
        order[item] = quantity
    else:
        print("Sorry, we don't have that item on our menu.")

total = sum(menu[item] * quantity for item, quantity in order.items())
print("\nYour total is: $", total)