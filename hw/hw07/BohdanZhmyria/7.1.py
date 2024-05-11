def biggest_num():
    """searching for biggest number"""
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    elif num1 == num2:
        print("The numbers are equal")

print(biggest_num())

