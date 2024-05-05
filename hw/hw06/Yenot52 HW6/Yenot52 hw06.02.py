#Task 2
correct_login = "First" # expected login name

while True:
    login = input("Enter yout login name: ")
    
    if login == correct_login:
        print("Welcome back, First!")
        break # exit the loop after successful login
    else:
        print("Error: Invalid login name.")  