from functions import rectangle_area, triangle_area, circle_area

def main():
    print("Choose the shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(a, b)
        print("The area of the rectangle is:", area)
    elif choice == 2:
        h = float(input("Enter the height of the triangle: "))
        a = float(input("Enter the base length of the triangle: "))
        area = triangle_area(h, a)
        print("The area of the triangle is:", area)
    elif choice == 3:
        r = float(input("Enter the radius of the circle: "))
        area = circle_area(r)
        print("The area of the circle is:", area)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()