n = int(input("Enter the number n: "))

fibonacci_sequence = [0, 1]

while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
    next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fibonacci)

print("Fibonacci sequence up to", n, ":", fibonacci_sequence)
