number = input('Enter the number')
product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
reverse = number[::-1]
ascend = sorted(number)

print('Product: ' + str(product))
print('Reverse: ' + str(reverse))
print('Ascend: ' + str(ascend))