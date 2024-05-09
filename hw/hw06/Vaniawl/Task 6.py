# # Task 6.1
# #Even numbers divisible by 2
# even_numbers_div_2 = [num for num in range(1 , 101) if num % 2 == 0]
# print(even_numbers_div_2)
# #Odd numbers divisible by 3"
# odd_numbers_div_3 = [num for num in range (1, 101) if num % 3 == 0 and num % 2 != 0]
# print(odd_numbers_div_3)
# #numbers that are not divisible by 2 and 3
# numbers_not_div_2_3 = [num for num in range (1, 101) if num % 3 != 0 and num % 2!= 0]
# print(numbers_not_div_2_3)

# Task 6.2
login = input("Enter your login: ")
attempts_for_login = 3
attempts_for_password = 3
password = "qwerty"

while attempts_for_login > 0:
    if login != "Vaniawl":
        print("Invalid login. Please try again.")
        login = input("Enter your login: ")
        attempts_for_login -= 1
        if attempts_for_login == 0:
            print("Sorry, but your account is temporarily blocked. Try to connect with our support team ")
    else:
        password_input = input("Enter your password: ")
        while password_input != password and attempts_for_password > 0:
            print("Invalid password. Please try again.")
            password_input = input("Enter your password: ")
            attempts_for_password -= 1
        if attempts_for_password == 0:
            print("Sorry, but your account is blocked. Try to connect with our support team ")
        else:
            print("You are logged in successfully!")
            break

