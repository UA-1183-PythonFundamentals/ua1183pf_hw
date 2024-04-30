#  given four-digit number
number = int(input("Enter a four-digit natural number: "))
digits = [int(digit) for digit in str(number)]

# product of the digits
product = 1
for digit in digits:
    product *= digit
print("Product of digits:", product)

# number in reverse order
reversed_number = int(str(number)[::-1])
print("Number in reverse order:", reversed_number)

# Sort the digits in ascending order
sorted_digits = sorted(digits)
print("Digits sorted in ascending order:", ''.join(map(str, sorted_digits)))