import math

def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

# Main program
shape = input("Please enter the shape (rectangle, triangle, or circle): ")

if shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("Area of rectangle:", rectangle_area(length, width))
elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("Area of triangle:", triangle_area(base, height))
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    print("Area of circle:", circle_area(radius))
else:
    print("Invalid shape entered.")
