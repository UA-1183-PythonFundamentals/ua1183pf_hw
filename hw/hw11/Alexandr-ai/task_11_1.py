def your_age():
    age = input('Input your age:')

    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age must be bigger then 0")
        if (age%2 == 0 and int(age) > 0):
            return print("Your have even number of an age")
        elif (age%2 == 1 and int(age) > 0):
            return print("Your have odd number of an age")
        
    except ValueError as e:
        print(f"Invalid input: {e}")

your_age()
