#Task 3
def factorial(n):
    if n < 0:
     print("Factorial id not defined for negative numbers.")
     return None
    if n == 0:
     return 1
    elif n == 1:
     return 1
 
    factorial = 1
    for i in range(2, n + 1):
     factorial *= i
     
    return factorial 

number = 5 
result = factorial(number)
if result is not None:
 print(f"The factorial of {number} is {result}")
 
 