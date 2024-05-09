even = []
odd = []
not_divisible = []

for i in range(10):
    if i%2:
        odd.append(i)
    if not i%2:
        even.append(i)
    if i%2 and i%3:
        not_divisible.append(i)

print(f'Even: {even}')
print(f'Odd: {odd}')
print(f'Not divisible by 2 and 3: {not_divisible}')
