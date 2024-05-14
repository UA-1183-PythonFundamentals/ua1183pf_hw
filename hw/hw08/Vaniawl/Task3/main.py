from shapes import rectangle_area, triangle_area, circle_area
from math import pi
def main ():
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        area = shapes.rectangle_area(length, width)
        print("Area of the rectangle: ", area)
    elif choice == 2:
        length = int(input("Enter the length of the triangle: "))
        width = int(input("Enter the width of the triangle: "))
        area = shapes.triangle_area(length, width)
        print("Area of the triangle: ", area)
    elif choice == 3:
        radius = int(input("Enter the radius of the circle: "))
        area = shapes.circle_area(radius)
        print("Area of the circle: ", area)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
