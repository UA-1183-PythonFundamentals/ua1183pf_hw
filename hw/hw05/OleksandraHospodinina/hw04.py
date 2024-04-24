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
