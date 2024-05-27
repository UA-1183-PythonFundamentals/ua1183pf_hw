class CustomErr(Exception):
    pass

def print_weekday(num:int):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        if num >= 8:
            raise CustomErr(f"Haven't weekday count {num}")
        elif num <= 0:
            raise CustomErr(f"Num of weekday can't be negative or zero")
        else:
            print(weekdays[num - 1])
    except CustomErr as err:
        print(err)
    

# Tests:
print_weekday(0)
print_weekday(-5)
print_weekday(3)
print_weekday(8)
print_weekday()
print_weekday('some string')
