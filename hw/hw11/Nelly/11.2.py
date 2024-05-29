# Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
# into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data

def get_day_of_week(number):
    days_of_week = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Субота",
        7: "Неділя"
    }
    return days_of_week.get(number, "Невідомий день тижня")

def main():
    try:
        user_input = input("Будь ласка, введіть номер дня тижня (1-7): ")
        number = int(user_input)
        if number < 1 or number > 7:
            print("Число має бути від 1 до 7.")
        else:
            day = get_day_of_week(number)
            print(f"День тижня: {day}")
    except ValueError:
        print("Помилка: введено нечислові дані. Будь ласка, введіть число від 1 до 7.")

if __name__ == "__main__":
    main()