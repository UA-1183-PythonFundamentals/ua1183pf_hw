import calculate_area

def main():
    print("Calculate Area of Figure")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        area = calculate_area.rectangle_area(length, width)
        print("Area of rectangle:", area)
    elif choice == 2:
        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))
        area = calculate_area.triangle_area(base, height)
        print("Area of triangle:", area)
    elif choice == 3:
        radius = float(input("Enter radius of circle: "))
        area = calculate_area.circle_area(radius)
        print("Area of circle:", area)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
