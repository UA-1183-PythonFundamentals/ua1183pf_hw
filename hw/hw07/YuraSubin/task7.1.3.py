def count_letter(word):
    count = {}
    for number in word:
        count[number] = count.get(number, 0) + 1
    return count
word = str(input("Please enter a word: "))
print(count_letter(word))