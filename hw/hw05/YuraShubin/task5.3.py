
num = int(input("Enter a namber to calculate a factoial : "))


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *=i
    return result

print(f"{num}!={factorial(num)}")