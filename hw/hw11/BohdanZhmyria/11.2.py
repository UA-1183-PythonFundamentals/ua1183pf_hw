def get_day_of_week():
    try:
        num = int(input("Enter a number (1-7) representing the day of the week: "))
        if num < 1 or num > 7:
            print("Please enter a number between 1 and 7.")
        else:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print(f"The day corresponding to {num} is {days[num - 1]}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    get_day_of_week()
