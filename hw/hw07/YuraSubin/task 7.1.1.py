def largest_number(num1, num2):
    """
    Return the largest number of two given numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2

# Example usage:
result = largest_number(5, 10)
print("The largest number is:", result)