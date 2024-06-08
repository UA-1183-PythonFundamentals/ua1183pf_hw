def get_day_of_week(day_number):
  days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  try:
    day_number = int(day_number)  # Convert input to integer (potential exception)
    return days_of_the_week[day_number % 7 - 1]  # Handle modulo by 7 for week mapping
  except ValueError:
    return "Invalid input: Please enter a number."

# Get user input
while True:
  day_number = input("Enter a number between 1 and 7 (or a higher number to see the pattern): ")
  result = get_day_of_week(day_number)
  print(result)
  break  # Exit after one input