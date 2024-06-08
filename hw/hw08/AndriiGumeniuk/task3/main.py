import utils

user_geometry = input("What geometry square do you need to calculate (Triangle, rectangle, circle)? ")

user_geometry = user_geometry.lower()

if user_geometry == "triangle":
    user_height = int(input("Enter height of triangle: "))
    user_base = int(input("Enter base of triangle: "))
    print(f"Square of triangle = {utils.square_of_triangle(user_height, user_base)}")
elif user_geometry == "rectangle":
    user_height = int(input("Enter height of rectangle: "))
    user_width = int(input("Enter width of rectangle: "))
    print(f"Square of rectangle = {utils.square_of_rect(user_height, user_width)}")
elif user_geometry == "circle":
    user_radius = int(input("Enter radius of circle: "))
    print(f"Square of circle = {utils.square_of_circle(user_radius)}")
else:
    print("data is not correct, try again")