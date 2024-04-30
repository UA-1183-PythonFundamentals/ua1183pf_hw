

a = '''The Zen of Python, by Tim Peters
    1.Beautiful is better than ugly.
    2.Explicit is better than implicit.
    3.Simple is better than complex.
    4.Complex is better than complicated.
    5.Flat is better than nested.
    6.Sparse is better than dense.
    7.Readability counts.
    8.Special cases aren't special enough to break the rules.
    9.Although practicality beats purity.
    10.Errors should never pass silently.
    11.Unless explicitly silenced.
    12.In the face of ambiguity, refuse the temptation to guess.
    13.There should be one-- and preferably only one --obvious way to do it.
    14.Although that way may not be obvious at first unless you're Dutch.
    15.Now is better than never.
    16.Although never is often better than *right* now.
    17.If the implementation is hard to explain, it's a bad idea.
    18.If the implementation is easy to explain, it may be a good idea.
    19.Namespaces are one honking great idea -- let's do more of those!
    20.Beautiful is better than ugly.
    21.Explicit is better than implicit.
    22.Simple is better than complex.
    23.Complex is better than complicated.
    24.Flat is better than nested.
    25.Sparse is better than dense.
    26.Readability counts.
    27.Special cases aren't special enough to break the rules.
    28.Although practicality beats purity.
    29.Errors should never pass silently.
    30.Unless explicitly silenced.
    31.In the face of ambiguity, refuse the temptation to guess.
    32.There should be one-- and preferably only one --obvious way to do it.
    33.Although that way may not be obvious at first unless you're Dutch.
    34.Now is better than never.
    35.Although never is often better than *right* now.
    36.If the implementation is hard to explain, it's a bad idea.
    37.If the implementation is easy to explain, it may be a good idea.
    38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
    39.Explicit is better than implicit.
    40.Simple is better than complex.
    41.Complex is better than complicated.
    42.Flat is better than nested.
    43.Sparse is better than dense.
    44.Readability counts.
    45.Special cases aren't special enough to break the rules.
    46.Although practicality beats purity.
    47.Errors should never pass silently.
    48.Unless explicitly silenced.
    49.In the face of ambiguity, refuse the temptation to guess.
    50.There should be one-- and preferably only one --obvious way to do it.
    51.Although that way may not be obvious at first unless you're Dutch.
    52.Now is better than never.
    53.Although never is often better than *right* now.
    54.If the implementation is hard to explain, it's a bad idea.
    55.If the implementation is easy to explain, it may be a good idea.
    56.Namespaces are one honking great idea -- let's do more of those!'''



count_better = a.count("better")
count_never = a.count("never")
count_is = a.count("is")
print("better:", count_better)
print("never:", count_never)
print("is:", count_is)

a_upper = a.upper()
#print(type(a))
print(a_upper)

b = '5234'

b_mult = int((b)[0]) * int((b)[1]) * int((b)[2]) * int((b)[3])
#print('mult number :', b_mult)
b_rev = ''.join(reversed(b))
b_sort = sorted(b)
#print("sorted number :", b_sort)
print('mult number :', b_mult, 'Reversed number' , b_rev, "sorted number :", b_sort)
print(set(b))


c_1 = 5
c_2 = 7
print('"c_1 number" :', c_1, '"c_2 number" :', c_2)
c_1, c_2 = c_2, c_1

print('"c_1 number changed" :', c_1, '"c_2 number changed" :', c_2)
