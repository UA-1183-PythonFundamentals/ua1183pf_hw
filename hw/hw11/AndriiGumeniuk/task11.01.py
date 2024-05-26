def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."


def main():
    try:
        age = int(input("Please enter your age: "))
        message = process_age(age)
        print(message)
    except ValueError as ve:
        print(f"Invalid input: {ve}")


if __name__ == "__main__":
    main()
