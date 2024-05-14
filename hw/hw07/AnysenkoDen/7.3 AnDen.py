def counter(word):
    count = {}
    for w in word:
        count[w] = count.get(w, 0) + 1
    return count

'''
Example
'''
print(counter('Collateral')) 