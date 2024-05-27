def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        return "The age is even."
    else:
        return "The age is odd."

def main():
    try:
        age = int(input("Enter your age: "))
        message = process_age(age)
        print(message)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
