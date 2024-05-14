import random


def guess_number():
    target_number = random.randint(1, 100)
    attempts = 10
    
    print("Welcome to the Number Lotery Game!")
    print("I have chosen a number between 1 and 100. You have 10 attempts to guess it. Jackpot is yours !!! ;)")
    
    while attempts > 0:
        guess = int(input("Enter your number: "))
        if guess == target_number:
            print("Congratulations! You win!")
            return
        elif guess < target_number:
            print("The number is greater than your guess.")
        else:
            print("The number is less than your guess.")
        attempts -= 1
    
    print("Sorry, you've used all your attempts. The number was:", target_number)

guess_number()