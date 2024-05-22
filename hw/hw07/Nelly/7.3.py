def count_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

input_str = "hello"
result = count_characters(input_str)
print(result)