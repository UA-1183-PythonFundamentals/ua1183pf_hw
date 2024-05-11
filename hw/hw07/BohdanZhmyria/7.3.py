def count_letters():
    """This function counts letters in words."""
    word = input("Enter a word: ")
    unique_letters = {}
    for letter in word:
        if letter in unique_letters:
            unique_letters[letter] += 1
        else:
            unique_letters[letter] = 1
    return unique_letters

print(count_letters())