# Task 1
print("Task 1:")
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even and divisible by 2.")
    if num % 2 != 0 and num % 3 == 0:
        print(f"{num} is odd and divisible by 3.")
    if num % 2 != 0 and num % 3 != 0:
        print(f"{num} is neither divisible by 2 nor 3.")

# Task 2
print("\nTask 2:")
while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Welcome, user!")
        break
    else:
        print("Error: Incorrect login. Please try again.")
