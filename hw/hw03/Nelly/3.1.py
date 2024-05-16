#3.1
a = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than right now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

better_count=a.lower().count("better")
print("Occurrences of 'better':", better_count)

uppercase_text = a.upper()
print("Text in uppercase:", uppercase_text)

replaced_text = a.replace("i", "&")
print("Text with 'i' replaced with '&", replaced_text)

#3.2
number = 1832
def new_func(number):
    product = 1
    for digit in str(number): product *= int(digit)
    print("Product of digits:", product)

    reversed_number = int(str(number)[::-1])
    print("Number in reverse order:", reversed_number)

    sorted_digits = int(''.join(sorted(str(number))))
    print("Digits in ascending order:", sorted_digits)

#3.3
    first_home = "Odesa"
    return first_home

first_home = new_func(number)
second_home = "Kyiv"

first_home  = (first_home  + second_home)
second_home  = first_home [len(first_home ) - len(second_home ):]
first_home  = first_home [:len(first_home ) - len(second_home )]

print(first_home)
print(second_home)




