number = int(input("Enter the number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is:", factorial)
