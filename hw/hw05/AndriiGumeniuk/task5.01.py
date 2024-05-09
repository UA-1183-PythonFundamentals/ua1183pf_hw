integer_list = [1, 2, 3, 4, 5]

float_list = []
for num in integer_list:
    float_list.append(float(num))

print("Original list:", integer_list)
print("List with elements converted to float:", float_list)
