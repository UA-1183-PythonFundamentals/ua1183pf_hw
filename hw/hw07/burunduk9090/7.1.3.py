def count_str(string):
    d = {}
    for i in range(len(string)):
        d[string[i]] = string.count(string[i])
    return d


print(count_str("hello world"))
