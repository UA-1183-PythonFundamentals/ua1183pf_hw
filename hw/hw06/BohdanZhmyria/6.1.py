#even numbers that are divisible by 2

for x in range(1, 11):
    if x % 2 == 0:
        print(x)

print("<<<")
print(">>>")

#odd numbers that are divisible by 3

for x in range(1, 11):
    if x % 3 ==0:
        print(x)

print("<<<")
print(">>>")
# #numbers that are not divisible by 2 and 3

for x in range(1, 11):
    if x % 2 != 0 and x % 3 != 0:
        print(x)
