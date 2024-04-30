number = 1234

# Find the product of the digits
product = 1
for digit in str(number):
    product *= int(digit)
print("Product of digits:", product)

# Write the number in reverse order
reverse_number = int(str(number)[::-1])
print("Number in reverse order:", reverse_number)

# Sort the digits in ascending order
sorted_digits = sorted(str(number))
sorted_number = int("".join(sorted_digits))
print("Number with digits sorted in ascending order:", sorted_number)