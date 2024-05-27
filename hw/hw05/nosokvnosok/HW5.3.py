n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n+1):
    print(f"{factorial} * {i} = ", end=" ")
    factorial = factorial * i
    print(factorial)
print(f"{n}! = factorial")
