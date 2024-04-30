# Function to generate Fibonacci sequence up to n
def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Get input from the user
n = int(input("Enter a number: "))

# Print Fibonacci sequence up to n
print("Fibonacci sequence up to", n, ":")
for num in fibonacci(n):
    print(num, end=" ")
