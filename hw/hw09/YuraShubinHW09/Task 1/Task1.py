import random

sec_number = random.randint(1, 100)


guess_number = int(input("Enter your number from 1 to 100: "))

x = 0

while guess_number != sec_number and x !=10:
    if guess_number <= sec_number:
        print("my number is higher")
    else:
        print("my number is lower")
    guess_number = int(input("Enter your number from 1 to 100: "))
    x += 1


if guess_number == sec_number:
    print(f"woow congratulation's you guess my secret number it's {sec_number}")
else:
    print(f"Come On.. you loose, you used all 10 attempts, the secret number was {sec_number}")


