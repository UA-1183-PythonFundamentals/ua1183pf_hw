#Task 1
numbers = range(1, 11)
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 3 == 0]
not_divisible = [num for num in numbers if num % 2 != 0 and num % 3 != 0]

print("Even numbers divisible by 2:", even_numbers)
print("Odd numbers divisible by 3:", odd_numbers)
print("Numbers not divisible by 2 and 3:", not_divisible)
