# Task 1

even_nums = []
odd_nums = []
not_disible_nums = []

for num in range(1, 11):
  if num % 2 == 0:
    even_nums.append(num)
  elif num % 3 == 0:
    odd_nums.append(num)
  elif num % 2 != 0 or num % 3 != 0:
    not_disible_nums.append(num)

print(f'Even nums are {even_nums}')
print(f'Odd nums are {odd_nums}')
print(f'not divisible by 2 or 3 are {not_disible_nums}')