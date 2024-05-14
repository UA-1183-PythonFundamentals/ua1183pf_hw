even = []
odd = []
exceptions= []
for num in range(1, 11):
    if num % 2 == 0:
        even.append(num)
    elif num % 3 == 0:
        odd.append(num)
    else:
        exceptions.append(num)
print("even / 2 ", even)
print("odd / 3 ", odd)
print("Exeptional numbers:", exceptions)