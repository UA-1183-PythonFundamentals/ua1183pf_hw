a = 'Oleksandr'
b = 20
print(f"a = {a}, b = {b}")
print(f"type a is {type(a)}, type b is {type(b)}")

a = [a, b]
print(f"'a' became the list and now is {a}, type(a) is {type(a)}")

b = a[0]
a = a[1]
print(f"a = {a}, b = {b}")
