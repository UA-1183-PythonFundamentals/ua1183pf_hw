#task 5.1
numbers = input("Enter your numbers using space separated: \n").split()
numbers = [int(num) for num in numbers]
for i in range(len(numbers)):
    numbers[i] = float(numbers[i])
print("Your numbers but in floating type: \n", numbers)

#task 5.2
n = int(input("Введіть число n: "))
a, b = 0, 1
print("Числа Фібоначчі до", n, ":", a, end=" ")
while b <= n:
    print(b, end=" ")
    a, b = b, a + b

#task 5.3
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n +1):
    factorial *= i
print(f"Factorial of {n} is : {factorial}")






