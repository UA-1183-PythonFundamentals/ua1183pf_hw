from calculate import rectangle_area, triangle_area, circle_area

def main():
    print("Choose the shape to calculate the area: \n1. Rectangle \n2. Triangle\n3. Circle")
    choice = input("Enter your choice (1, 2, 3): ")
    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print("The area of the rectangle is:", area)
    elif choice == '2':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(height, base)
        print("The area of the triangle is:", area)
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print("The area of the circle is:", area)
    else:
        print("Invalid choice!")
main()