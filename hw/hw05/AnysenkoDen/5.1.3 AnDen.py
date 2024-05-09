num = input('Enter your number')
a = int(num)
num = int(num)
if a == 0:
    print('1')
else: 
    while a != 1:
        a = a - 1
        num = num * a
print(num)