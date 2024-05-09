needed = input('Enter the number')
fib = [0, 1]
a = 0
while int(fib[-1]) < int(needed):
    a = fib[-1] + fib[-2]
    fib.append(a)
print(fib)