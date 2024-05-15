import random
counter = 0
user_name = input("Hello! What's your name? \n")

number = random.randint(1,100)
while counter < 10:

  guess_number = int(input("Enter your number from range: 1 to 100:"))
  counter += 1
  if guess_number == number:
    print(f"Good job, {user_name}! You are winner!")
    break
  elif 1<= guess_number <= 100 and guess_number < number and counter < 10:
    print ("Your number is less. Try again")
  elif 1<= guess_number <= 100 and guess_number > number and counter < 10:
    print (f"Your number is more. Try again, {user_name}")
  elif not 1<= guess_number <= 100 and counter < 10 :
    print ("Your number is not in range 1 to 100. Try again")
  while counter == 10:
    print("Sorry, you have used all your attempts!")
    break
print(f"Thank you for playing {user_name}!")