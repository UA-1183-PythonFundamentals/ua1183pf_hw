def triangle_area(length, width):
    """This function calculates the area of a triangle."""
    return 0.5 * length * width

def rectangle_area(base, height):
    """This function calculates the area of a rectangle."""
    return base * height

def circle_area(radius):
    """This function calculates the area of a circle."""
    return 3.14 * radius ** 2

def main_app():
    """This function runs the main application."""
    print("Do you want to know area of rectangle, triangle or circle?")
    user_answer = input().lower()
    if user_answer == 'rectangle':
        base = float(input("Enter the base length of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        print("The area of the rectangle is:", rectangle_area(base, height))
    elif user_answer == 'triangle':
        length = float(input("Enter the length of the base of the triangle: "))
        width = float(input("Enter the height of the triangle: "))
        print("The area of the triangle is:", triangle_area(length, width))
    elif user_answer == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        print("The area of the circle is:", circle_area(radius))
    else:
        print("Sorry, I don't understand your input")

main_app()