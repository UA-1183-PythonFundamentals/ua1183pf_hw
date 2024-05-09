#Task 2
def fibonacci(n):
  if n < 0:
    print("Invalid input. Please enter non-negative integer.")    
  
  a, b = 0, 1 #initialize the first two Fibonacci numbers

  if n >= 1:
     print(a)
  if n >= 2:
     print(b)

  for i in range(2, n):
     c = a + b #calculate the next Fibonacci numbers 
     print(c)
     a, b = b, c
try:    
  n = int(input("Enter the number of terms (non-negative integer): "))
  fibonacci(n)
except ValueError:
  print("Invalid input. Please enter a non-negative integer.")