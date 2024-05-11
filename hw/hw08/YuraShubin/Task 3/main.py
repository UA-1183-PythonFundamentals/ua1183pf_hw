from backstage import *


def main():
    print("Hi there.. can you chose the figure? "
          "\n1 is rectangle; \n2 is triangle; \n3 is circle. \nSo make your choise: 1 or 2 or 3: ")
    choice = input("Enter your choice (1, 2, 3): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle(length, width)
        print("The area of the rectangle is:", area)
    elif choice == '2':
        high = float(input("Enter the high of the triangle: "))
        width = float(input("Enter the width of the triangle: "))
        area = triangle(high, width)
        print("The area of the rectangle is:", area)
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = circle(radius)
        print("The area of the rectangle is:", area)


main()
