#4
#1
a = 0
while a < 100:
    if a % 2 == 0:
        print(a)
    a += 2

for a in range(0, 99, 2):
    print(a)

#2
a = 1
for a in range(1, 100, 2):
    print(a)

for a in range(1, 100, 2):
    if a % 2 == 0:
        continue
    print(a)

#3
def odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            return True
    return Fasle

#4.1
a = [11, 45, 658]
for b in range(len(a)):
    a[b] = float(a[b])
print(a)

#4.2
x = int(input("Enter a number: "))
a, b = 0, 1
for i in range(0, x + 1):
    print(i, '=>', a)
    a, b = b, a + b

#4.3

num = int(input("Enter a number: "))
def factorial(num):
    fac = 1
    for a in range(1, num + 1):
        fac *= a
    return fac

print(f"{num}! =", factorial(num))
