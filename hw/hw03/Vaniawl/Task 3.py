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
#----
print("Number of occurrence of better: ", Zen.count("better"))
print("Number of occurrence of never: ", Zen.count("never"))
print("Number of occurrence of is: ", Zen.count("is"))
#----
print(Zen.upper())
#----
print(Zen.replace('i', '&'))

# Task 3.2
number = input("Enter a 4 digit number: ")
if int(number) != 4:
    print("Invalid input")
product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print(product)

reversed_string = number[::-1]
print(reversed_string)

print(sorted(number))


# Task 3.3

a = int(input("a =" ))
b = int(input("b =" ))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)








