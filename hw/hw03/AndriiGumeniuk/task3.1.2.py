number = 3956

product = 1
for digit in str(number):
    product *= int(digit)

reversed_number = int(str(number)[::-1])

sorted_digits = ''.join(sorted(str(number)))

print("Product of digits:", product)
print("Number in reverse order:", reversed_number)
print("Digits in ascending order:", sorted_digits)
