even = []
noteven = []
everything = []

for num in range(1, 11):
    if num %2 == 0:
        even.append(num)
    elif num %2 != 0 and num %3 == 0:
        noteven.append(num)
    elif num %2 != 0 and num %3 != 0:
        everything.append(num)

print(f"All even number: {even}")
print(f"All noteven number: {noteven}")
print(f"All everything number: {everything}")




