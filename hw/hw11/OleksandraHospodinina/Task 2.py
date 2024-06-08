class DayError(Exception):
    pass


class DaysOfWeek:
    def __init__(self, num):
        self.num = num

    def day_of_the_week(self):
        if not isinstance(self.num, int):
            raise DayError("Input must be a number")
        elif self.num == 1:
            print("Monday")
        elif self.num == 2:
            print("Tuesday")
        elif self.num == 3:
            print("Wednesday")
        elif self.num == 4:
            print("Thursday")
        elif self.num == 5:
            print("Friday")
        elif self.num == 6:
            print("Saturday")
        elif self.num == 7:
            print("Sunday")
        elif self.num < 1:
            raise DayError("The day of the week number must be between 1 and 7")
        elif self.num > 8:
            raise DayError("The day of the week number must be between 1 and 7")


try:
    num = int(input("Enter a number of the day of the week: "))
    day_input = DaysOfWeek(num)
    result = day_input.day_of_the_week()

except ValueError:
    print("Error: Input must be a number")
except DayError as e:
    print(e)
