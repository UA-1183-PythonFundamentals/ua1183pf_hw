main = True
login = []

while main:
    print("\n if you even stop, write <Stop>\n")

    name = input("Enter your name: ")

    if name == 'Stop':
        main = False
    elif not login:
        login.append(name)
        print(f"Hello, {name}")
    elif name in login:
        print(f"Welcome back, {name}")
    else:
        print("Please, try again!)")