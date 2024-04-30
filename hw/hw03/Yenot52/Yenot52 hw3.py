phylosophy = ("Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\n\
Complex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\n\
Special cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\n\
Unless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\n\
Although that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\n\
If the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\n\
Namespaces are one honking great idea -- let's do more of those!")

#1.1

better_count = phylosophy.count("better")
never_count = phylosophy.count("never")
is_count = phylosophy.count("is")

#1.2

uppercase_phylosophy = phylosophy.upper()

#1.3

replaced_phylosophy= uppercase_phylosophy.replace("I", "&")

print(f"Counts: better - {better_count}, never - {never_count}, is - {is_count}")
print(f"Uppercase: {uppercase_phylosophy}")
print(f"Replaced 'i' with '&': {replaced_phylosophy}")

#2.1

def analyze_number(number):
  """Analyzes a four-digital integer.
  Args: 
      number: A four-digit integer
  
  Returns:
      A tuple containing:
          - The product of the digits.
          - The number in reverse order.
          - The digits serted in ascending order.
  """
  if not (1000 <= number <= 9999):
    raise ValueError("Input must be a four-digital number")
  
  digits = [int(d) for d in str(number)]
  
  product = 1
  for digit in digits: 
    product *= digit
    
  #2.2 and 2.3 
  
  reversed_number = int(str(number)[::-1]) 
  
  sorted_digits = sorted(digits)
  
  return product, reversed_number, sorted_digits
number = 5678
product, reversed_number, sorted_digits = analyze_number(number)
print(f"Product of digits: {product}")
print(f"Number in reverse order: {reversed_number}")
print(f"Digits sorted in asceding order:{sorted_digits}")

#3 

def swap_without_temp(a, b): 
  """Swaps the values of the two variable using arithmetic operations.
  
  Args:
      a: The first variable. 
      b: The second variable.
  """
  a = a + b   # This adds the value of b to a.
  b = a - b   # Subtract the original b from the new a 
  a = a - b   # Subtract the new b from the new a
  
#Example
x = 5 
y = 10
swap_without_temp(x, y)
print(f"x: {x}, y: {y}")