def count_characters(input_string):
    """
    Calculate the number of characters included in the given string.

    Args:
        input_string (str): The input string.

    Returns:
        dict: A dictionary containing each character of the string as keys
              and their respective counts as values.
    """
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Test the function
input_str = "hello"
print(count_characters(input_str))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
