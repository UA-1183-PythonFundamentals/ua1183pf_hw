week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
number = int(input('Enter a number: '))  # takes into account non-numeric data

match number:
    case 1:
        print(week[number - 1])
    case 2:
        print(week[number - 1])
    case 3:
        print(week[number - 1])
    case 4:
        print(week[number - 1])
    case 5:
        print(week[number - 1])
    case 6:
        print(week[number - 1])
    case 7:
        print(week[number - 1])
    case _:
        raise ValueError('Invalid input')  # takes into account numbers larger and smaller than allowed
