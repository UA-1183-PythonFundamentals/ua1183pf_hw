import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)   
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

    for attempt in range(1, attempts + 1):
        number = int(input(f"Attempt {attempt}: Enter your number: "))

        if number < number_to_guess:
            print("The number is higher than your number.")
        elif number > number_to_guess:
            print("The number is lower than your number.")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            return   

    print(f"You've used all {attempts} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
