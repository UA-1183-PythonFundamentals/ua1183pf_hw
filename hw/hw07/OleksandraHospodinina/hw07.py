#1
def arithmetic_mean(*numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean
    if not args:
        return 0
numbers = [11, 51, 114]
mean = arithmetic_mean(*numbers)
print(mean)

#4.1.1
def largest(num1, num2):
    """ This function finds the largest number of two numbers
    :param num1: int or float
    :param num2:int or float
    :return: the largest number """
    return max(num1, num2)
maximum = largest(45, 45.61)
print(maximum)

#4.1.2
def triangle_area(base, height):
    return base * height
def rectangle_area(side1, side2):
    return side1 * side2
def circle_area(radius):
    PI = 3.14
    return PI * (radius ** 2)
def main():
    print("1. Triangle area.")
    print("2. Rectangle area.")
    print("3. Circle area.")
    user = input("Choose which area to search (1, 2, 3): ")
    if user == "1":
        base = float(input("Base: "))
        height = float(input("Height: "))
        area1 = triangle_area(base, height)
        print("Area = ", area1)
    elif user == "2":
        side1 = float(input("Side 1: "))
        side2 = float(input("Side 2: "))
        area2 = rectangle_area(side1, side2)
        print("Area = ", area2)
    elif user == "3":
        radius = float(input("Radius: "))
        area3 = circle_area(radius)
        print("Area = ", area3)
    else:
        print("Choose 1, 2 or 3! ")

main()

#4.1.3
def count_letters(word):
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1
    return count
word = str(input("Enter a word: "))
print(count_letters(word))
