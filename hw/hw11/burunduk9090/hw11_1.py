def main():
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Invalid age")
    print('Even ' if age % 2 == 0 else 'Odd')


if __name__ == '__main__':
    main()
