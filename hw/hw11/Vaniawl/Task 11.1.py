def check_age():
    try:
        age=int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age % 2 == 0:
            print("Your age is an even number")
        else:
            print("Your age is an odd number")
    except ValueError as ve:
        print("Error", ve)

if __name__ == "__main__":
    check_age()