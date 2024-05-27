def check_age(age):
  if age < 0:
    raise ValueError("Age cannot be negative.")

  parity = "even" if age % 2 == 0 else "odd"
  print(f"Your age is {parity}.")

# Main program loop
while True:
  try:
    age = int(input("Enter your age: "))
    check_age(age)
    break  # Exit the loop after successful input
  except ValueError as e:
    print(f"Error: {e}")
    print("Please enter a valid non-negative integer for your age.")