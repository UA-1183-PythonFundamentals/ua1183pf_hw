import math

def calculate_area():
    shape = input("Choose the shape (rectangle, triangle, circle): ").strip().lower()

    if shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width

    elif shape == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height

    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        area = math.pi * radius * radius

    else:
        print("Invalid shape.")
        return

    print(f"The area of the {shape} is: {area}")

if __name__ == "__main__":
    calculate_area()
