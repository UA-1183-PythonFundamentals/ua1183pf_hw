limit = int(input("Enter a number: "))
fact = 1

for i in range(1, limit+1):
    fact*=i
    print(f"factorial: {fact}")
