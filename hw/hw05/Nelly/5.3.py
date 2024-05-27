num = int(input("Enter a number: "))
factorial_ = 1

for i in range(1, num + 1):
    factorial_ *= i

print("The factorial of", num, "is", factorial_)