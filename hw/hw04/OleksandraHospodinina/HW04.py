#Task 4

#1
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1 > num2:
    print(f"number 1 ({num1}) > number 2 ({num2})")
elif num1 < num2:
    print(f"number 1 ({num1}) > number 2 ({num2})")
else:
    print(f"number 1 ({num1}) = number 2 ({num2})")

#2
num = int(input("Enter number: "))
if num % 2 == 0:
    print(f"Number {num} is even number")
else:
    print(f"Number {num} is odd number")