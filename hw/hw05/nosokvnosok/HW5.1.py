elements = int(input("Enter number of elements: "))
intList = []
floatList = []

for i in range(elements):
    intList.append(int(input("Enter element: ")))
print(intList, type(intList[0]))

for num in intList:
    floatList.append(float(num))

print(intList, type(intList[0]))
print(floatList, type(floatList[0]))
