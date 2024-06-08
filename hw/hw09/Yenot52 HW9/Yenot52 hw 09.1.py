import random

secret_number = random.randint(1, 100)

# Initialize attempts counter
attempts = 0

while attempts < 10:
  try:
    guess = int(input(f"Guess the number (attempt {attempts+1} of 10): "))
  except ValueError:
    print("Invalid input. Please enter an integer.")
    continue  # Skip to the next iteration if input is not an integer

  # Check the guess
  attempts += 1
  if guess == secret_number:
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    break  # Exit the loop if guess is correct

  # Provide hint based on guess
  elif guess < secret_number:
    print("Your guess is too low. Try again.")
  else:
    print("Your guess is too high. Try again.")

# User ran out of attempts
if attempts == 10:
  print(f"Sorry, you ran out of attempts. The secret number was {secret_number}.")