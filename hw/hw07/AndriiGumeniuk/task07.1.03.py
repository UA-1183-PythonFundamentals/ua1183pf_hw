def count_letters(word):
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1
    return count
word = str(input("Enter a word: "))
print(count_letters(word))