def weekday():
    try:
        num = int(input("Enter a number (1-7) to get the corresponding day of the week: "))
        if 1 <= num <= 7:
            days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
            print(f"The day corresponding to the number {num} is {days[num]}.")
        else:
            print("Invalid input")
    except ValueError:
        print("Please enter a valid numerical input")
if __name__ == "__main__":
    weekday()