def char_count(text):
  """Calculates the number of occurrences of each character in a string.

  Args:
    text: The string to count the characters of.

  Returns:
    A dictionary mapping each character to its number of occurrences.
  """
  return {char: text.count(char) for char in text}

#Example
text = "hello"
char_counts = char_count(text)
print(char_counts)