n = int(input("Enter a number: "))

numbers = [0,1]

for i in range(2, n+1):
    number = numbers[i-1]+ numbers[i-2]
    numbers.append(number)

#     if number > n:        не до кінця зрозумів, тому лишив це тут
#         break

print("fib to n: ", numbers)