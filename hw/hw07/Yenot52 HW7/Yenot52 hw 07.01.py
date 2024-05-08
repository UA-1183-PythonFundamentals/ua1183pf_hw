def largest_number(num1, num2):
  """This function takes two numbers as input and returns the largest number.
  
  Args:
    num1: The first number.
    num2: The second number.

  Returns: The largest number. 
  """
  if num1 > num2:
    return num1
  else:
    return num2 

#Example of usage 
result = largest_number(5, 4)
print(result)  