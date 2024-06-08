import random

def guess_number():

    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. You have 10 attempts to guess it.")

    while attempts < 10:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == target_number:
            print("Congratulations! You guessed the number {} in {} attempts.".format(target_number, attempts))
            return
        elif guess < target_number:
            print("The number I picked is greater than your guess.")
        else:
            print("The number I picked is less than your guess.")

    print("Sorry, you've used all 10 attempts. The number I picked was {}.".format(target_number))

guess_number()
