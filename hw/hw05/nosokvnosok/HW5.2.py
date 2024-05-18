n = int(input("Enter the number up to which you want to print Fibonacci numbers: "))

fibonacci_sequence = [0, 1]

print("Fibonacci numbers up to", n, ":")
print(fibonacci_sequence[0])
print(fibonacci_sequence[1])

while True:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    if next_number > n:
        break
    fibonacci_sequence.append(next_number)
    print(next_number)
