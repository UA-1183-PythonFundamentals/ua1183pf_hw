# Task 6.1
#Even numbers divisible by 2
even_numbers_div_2 = [num for num in range(1 , 101) if num % 2 == 0]
print(even_numbers_div_2)
#Odd numbers divisible by 3"
odd_numbers_div_3 = [num for num in range (1, 101) if num % 3 == 0 and num % 2 != 0]
print(odd_numbers_div_3)
#numbers that are not divisible by 2 and 3
numbers_not_div_2_3 = [num for num in range (1, 101) if num % 3 != 0 and num % 2!= 0]
print(numbers_not_div_2_3)

def login():
    correct_username = "user123"
    correct_password = "password123"

    entered_username = input("Введіть логін: ")
    entered_password = input("Введіть пароль: ")

    if entered_username == correct_username and entered_password == correct_password:
        print("You are logged in!")
    else:
        print("Login or password is not correct")

login()