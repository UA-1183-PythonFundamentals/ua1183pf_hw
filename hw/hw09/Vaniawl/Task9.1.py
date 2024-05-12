import random


def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Hi! Do you want to play?")
    print("I've picked a number between 1 and 100. Try to guess it. But remember, You have only 10 attempts")
    while attempts < 10:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            play_again = input("Congrats! You guessed the correct number!"
                               "Do you want to play again? Just type 'yes' or 'no'")
            if play_again == "yes":
                guess_number()
            else:
                print("Thank you for playing!")
        if guess < secret_number:
            print("Your guess is too low.")
            attempts += 1
        if guess > secret_number:
            print("Your guess is too high.")
            attempts += 1

    attempts > 10
    play_again1 = input(
        f"Sorry, you lost. The correct answer was {secret_number}. But you can try again. Do you want to play "
        f"again? Just type 'yes' or 'no'")
    if play_again1 == "yes":
        guess_number()
    else:
        print("Thanks for the game!")


guess_number()
