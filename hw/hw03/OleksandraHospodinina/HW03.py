zen = str("Beautiful is better than ugly.\nExplicit is better than implicit.\n\
Simple is better than complex.\nComplex is better than complicated.\n\
Flat is better than nested.\nSparse is better than dense.\n\
Readability counts.\nSpecial cases aren't special enough to break the rules.\n\
Although practicality beats purity.\nErrors should never pass silently.\n\
Unless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\n\
There should be one-- and preferably only one --obvious way to do it.\n\
Although that way may not be obvious at first unless you're Dutch.\n\
Now is better than never.\nAlthough never is often better than *right* now.\n\
If the implementation is hard to explain, it's a bad idea.\n\
If the implementation is easy to explain, it may be a good idea.\n\
Namespaces are one honking great idea -- let's do more of those!")

#3.1
print(zen)

#3.1.1
count1 = zen.count("better")
print(count1)
count2 = zen.count("never")
print(count2)
count3 = zen.count("is")
print(count3)

#3.1.2
print(str.upper(zen))

#3.1.3
zen_new = zen.replace("i", "&")
print(zen_new)

#3.2.1
a = int(1547)
print(a)

if 1000 <= a <= 9999:
   a1 = 1
while a > 0:
    digit = a % 10
    a1 *= digit
    a //= 10
print(a1)

#3.2.2
b = int(1547)
if 1000 <= b <= 9999:
   b1 = 0
while b > 0:
    digit = b % 10
    b = b // 10
    b1 = b1 * 10 + digit
print(b1)

#3.2.3

a = 1547
a1 = list(str(a))
print(a1)
print(sorted(a1))

#3.3

#1
a = int(input("a =" ))
b = int(input("b =" ))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

#2
c = input("c is: ")
d = input("d is: ")
print(c, d)

c = [c, d]
d = c[0]
c = c[1]
print(c,d)
