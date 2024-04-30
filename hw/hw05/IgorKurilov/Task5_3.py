# Function to calculate factorial without recursion
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get input from the user
n = int(input("Enter a number: "))

# Calculate factorial of n
fact = factorial(n)

# Print the result
print(f"{n}! =", fact)
