#Task 7.1.1
def largest_number(numbers):
    """введеня будь якої кількості чисел для визначення найбільшого"""
    #конвертація рядка в список
    numbers_list = [int(num) for num in numbers.split()]


    largest = max(numbers_list)
    return largest

numbers = input("Enter numbers, as much, as you want, using space: \n")
result = largest_number(numbers)
print(result)




# Task 7.1.2
import math
def area_of_rectangle(length, width):
    return length * width


def area_of_triangle(base, height):
    return 1 / 2 * base * height


def area_of_circle(radius):
    return math.pi * radius ** 2


def main():
    print("What do you want to calculate?")
    print("1. Area of rectangle \n"
          "2. Area of triangle \n"
          "3. Area of circle \n"
          )
    choice = input("Enter your choice: \n ")

    if choice == "1":
        height = float(input("Enter the height: \n "))
        length = float(input("Enter the length: \n "))
        area = area_of_rectangle(length, height)
        print("Area of rectangle", area)

    elif choice == "2":
        height = float(input("Enter the height: \n "))
        width = float(input("Enter the width: \n "))
        area = area_of_triangle(height, width)
        print("Area of triangle", area)

    elif choice == "3":
        radius = float(input(" Enter the radius: \n "))
        print("Area of circle", round(area_of_circle(radius), 2))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

Task 7.1.3
def count_chars(string):
    count = {}
    for c in string:
        count[c] = count.get(c, 0) + 1
    return count
input_string = input("Enter a string: \n")
result = count_chars(input_string)
print(result)
