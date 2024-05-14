import random

secret_number = random.randint(1, 100)
print(secret_number)

guess_number = int(input("Guess a number between 1 and 100: "))
i = 0

while guess_number != secret_number and i != 10:
    if guess_number > secret_number:
        print("Guess higher")
    else:
        print("Guess lower")
    guess_number = int(input("Guess a number between 1 and 100: "))

    i += 1

if guess_number == secret_number:
    print("Congrats! You guessed the secret number!")
else:
    print("Sorry, you've used every attempt ")
