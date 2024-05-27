import random


def guess():
    guesses = 1
    number = random.randint(1, 100)
    print("Guess the number between 1 and 100")
    while guesses <= 11:
        guess = int(input("Attempt numer " + str(guesses) + " "))
        if guess == number:
            play_again = print("Congratulations!")
            break
        if guess < number:
            print("The number is higher.")
            guesses += 1
        if guess > number:
            print("The number is lesser.")
            guesses += 1
        if guesses == 11:
            print("You have outnumbered your guesses. The number was " + str(number) + ". Wanna try again?")
            return True


if guess() == True:
    restart = input()
    if restart == "yes":
        guess()