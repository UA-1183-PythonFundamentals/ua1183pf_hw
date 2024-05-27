def get_day_of_week():
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    user_input = input("Enter a day number of the week:")
    
    try:
        number = int(user_input)
        
        if number in days_of_week:
            print(f"The day corresponding to number {number} is {days_of_week[number]}.")
        else:
            print("Please enter a number from 1 to 7")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

get_day_of_week()