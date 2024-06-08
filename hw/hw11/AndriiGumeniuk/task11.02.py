def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(number, "Invalid number. Please enter a number between 1 and 7.")

def main():
    try:
        user_input = input("Please enter a number to get the day of the week: ")
        number = int(user_input)
        day = get_day_of_week(number)
        print(day)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()