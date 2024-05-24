def get_day_of_week(number):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if number in days_of_week:
        return days_of_week[number]
    else:
        return "Invalid number for day of the week. Please enter a number between 1 and 7."

def main():
    try:
        number = int(input("Enter a number (1-7) to get the corresponding day of the week: "))
        message = get_day_of_week(number)
        print(message)
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()
