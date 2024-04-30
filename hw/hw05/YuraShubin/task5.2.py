f1 = 0
f2 = 1


n = int(input("Enter number: "))
print(f1, f2, end=' ')

while n > 1:
    if n > f1 and n > f2:
        f1, f2 = f2, f1 + f2
        print(f2, end=' ')
        n -=1