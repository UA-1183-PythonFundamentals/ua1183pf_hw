# Task 3.1
Zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
print("Number of occurrence of better:", Zen.count("better"))
print("Number of occurrence of never:", Zen.count("never"))
print("Number of occurrence of is:", Zen.count("is"))

uppercase_text = Zen.upper()
print(uppercase_text)

print (Zen.replace('i', '&'))

# Task 3.2
num = input("Enter a 4-digit number: ")
if len(num) == 4:
    print(int(num[0])*int(num[1])*int(num[2])*int(num[3]))
else:
    print ("Invalid input")

reversed_order = num[::-1]
print(reversed_order)

print(sorted(num))

# Task 3.3
a = int(input("a =" ))
b = int(input("b =" ))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)
