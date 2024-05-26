import shapes

def main():
    print("Which figure's area do you want to calculate?")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        area = shapes.rectangle_area(a, b)
        print("Area of the rectangle:", area)
    elif choice == '2':
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = shapes.triangle_area(a, h)
        print("Area of the triangle:", area)
    elif choice == '3':
        r = float(input("Enter the radius of the circle: "))
        area = shapes.circle_area(r)
        print("Area of the circle:", area)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
