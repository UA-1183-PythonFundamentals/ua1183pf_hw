input_str = "hello"

def count_letteracters(input_string):
    letter_count = {}
    for letter in input_string:
        # letter_count[letter] = letter_count.get(letter, 0) + 1 
        letter_count[letter] = input_str.count(letter)
    return letter_count

result = count_letteracters(input_str)
print(result)