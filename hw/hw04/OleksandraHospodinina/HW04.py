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

#4.1
c = float(input("Enter a temperature in Celsius: "))
a = float(0 - 273.15)

if c >= a:
    f = int(c * 9 / 5 + 54)
    print(f"Enter the temperature in Celsius: {c}")
    print(f" {c}°C is equivalent to {f}°F")
else:
    print(f"Enter the temperature in Celsius: {c}")
    print("Error: Temperature below absolute zero (-273.15°C)")