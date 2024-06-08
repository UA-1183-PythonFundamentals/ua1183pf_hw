def get_day_of_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if number < 1 or number > 7:
        return "Invalid input. Please enter a number between 1 and 7."
    else:
        return days[number - 1]

def main():
    while True:
        try:
            user_input = input("Enter a number (1-7) to get the corresponding day of the week, or 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Exiting program.")
                break
            else:
                number = int(user_input)
                print("Day of the week:", get_day_of_week(number))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7 or 'exit' to quit.")

if __name__ == "__main__":
    main()