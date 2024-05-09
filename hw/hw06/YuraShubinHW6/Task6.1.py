n = range(1, 10)

print(n)

even = []
odd = []
not_divisible = []

for i in n:
    if i%2 == 0:
        even.append(i)
    elif i%3 == 0:
        odd.append(i)
    elif i%2 != 2 and i%3 != 3:
        not_divisible.append(i)

print('even' , even)
print('odd' , odd)
print('not_divisible' , not_divisible)