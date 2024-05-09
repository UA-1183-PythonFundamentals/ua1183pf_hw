a = int(1547)
print(a)
if 1000 <= a <= 9999:
    a1 = 1
    while a > 0:
        digit = a % 10
        a1 *= digit
        a //= 10
print(a1)
b = int(1547)
if 1000 <= b <= 9999:
    b1 = 0
    while b > 0:
        digit = b % 10
        b = b // 10
        b1 = b1 * 10 + digit
print(b1)
a = 1547
a1 = list(str(a))
print(a1)
print(sorted(a1))