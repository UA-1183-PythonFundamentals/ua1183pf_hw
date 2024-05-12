def main_app():
    """This function runs the main application."""
    print("Do you want to know area of rectangle, triangle or circle?")
    user_answer = input().lower()
    if user_answer == 'rectangle':
        base = float(input("Enter the base length of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        from functions import rectangle_area
        print("The area of the rectangle is:", rectangle_area(base, height))
    elif user_answer == 'triangle':
        length = float(input("Enter the length of the base of the triangle: "))
        width = float(input("Enter the height of the triangle: "))
        from functions import triangle_area
        print("The area of the triangle is:", triangle_area(length, width))
    elif user_answer == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        from functions import circle_area
        print("The area of the circle is:", circle_area(radius))
    else:
        print("Sorry, I don't understand your input")


main_app()