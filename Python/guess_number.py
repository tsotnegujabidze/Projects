import random

range = int(input("Enter the range you want to guess with in> "))

print(f"guess number beetwen 1 and {range}, 0 doesn't count!")

number = random.randint(1 , range)

guess = None

while guess != number:
    guess = int(input("Enter your guess> "))
    if guess < number:
        print("Try Higher!")
    elif guess > number:
        print("Try Lower!")

print("You are correct!")